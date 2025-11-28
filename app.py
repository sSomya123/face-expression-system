from flask import Flask, render_template, Response, jsonify
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import os

app = Flask(__name__)

# Emotion labels (standard FER2013 emotions)
EMOTIONS = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Load face cascade classifier
cascade_path = 'haarcascade_frontalface_default.xml'
if os.path.exists(cascade_path):
    face_cascade = cv2.CascadeClassifier(cascade_path)
else:
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Global variable for model
emotion_model = None

def load_emotion_model():
    """Load emotion detection model from local directory"""
    global emotion_model
    
    model_path = 'models/emotion_model.h5'
    
    if not os.path.exists(model_path):
        print(f"Error: Model file not found at {model_path}")
        print("Please ensure emotion_model.h5 is in the models/ directory")
        return None
    
    try:
        print(f"Loading emotion model from {model_path}...")
        emotion_model = load_model(model_path, compile=False)
        print("✓ Emotion model loaded successfully!")
        return emotion_model
    except Exception as e:
        print(f"✗ Error loading model: {e}")
        return None

def detect_emotion(face_roi):
    """
    Detect emotion from face region of interest
    Similar to DeepFace.analyze() but using our local model
    """
    if emotion_model is None:
        return "Model Error", 0.0, {}
    
    try:
        # Preprocess the face (convert to grayscale and resize to 64x64)
        gray_face = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
        resized_face = cv2.resize(gray_face, (64, 64))
        normalized_face = resized_face.astype("float") / 255.0
        
        # Prepare for model input
        face_array = img_to_array(normalized_face)
        face_array = np.expand_dims(face_array, axis=0)
        
        # Predict emotion
        predictions = emotion_model.predict(face_array, verbose=0)[0]
        
        # Get dominant emotion
        emotion_idx = np.argmax(predictions)
        dominant_emotion = EMOTIONS[emotion_idx]
        confidence = float(predictions[emotion_idx])
        
        # Create emotion scores dictionary (like DeepFace)
        emotion_scores = {
            EMOTIONS[i].lower(): float(predictions[i] * 100) 
            for i in range(len(EMOTIONS))
        }
        
        return dominant_emotion, confidence, emotion_scores
    
    except Exception as e:
        print(f"Error detecting emotion: {e}")
        return "Unknown", 0.0, {}

def generate_frames():
    """Generate video frames with emotion detection"""
    camera = cv2.VideoCapture(0)
    
    if not camera.isOpened():
        print("Error: Could not open webcam")
        return
    
    while True:
        success, frame = camera.read()
        if not success:
            break
        
        # Convert to grayscale for face detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = face_cascade.detectMultiScale(
            gray_frame, 
            scaleFactor=1.1, 
            minNeighbors=5, 
            minSize=(30, 30)
        )
        
        for (x, y, w, h) in faces:
            # Extract the face ROI (Region of Interest)
            face_roi = frame[y:y+h, x:x+w]
            
            # Perform emotion analysis on the face ROI
            emotion, confidence, scores = detect_emotion(face_roi)
            
            # Draw rectangle around face (red color like DeepFace example)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            
            # Display emotion label and confidence
            label = f"{emotion}: {confidence:.2%}"
            cv2.putText(frame, label, (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            
            # Optionally show top 3 emotions
            if scores:
                sorted_emotions = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
                y_offset = y + h + 20
                for emo, score in sorted_emotions:
                    score_text = f"{emo}: {score:.1f}%"
                    cv2.putText(frame, score_text, (x, y_offset), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                    y_offset += 20
        
        # Encode frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
    camera.release()

@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Video streaming route"""
    return Response(generate_frames(), 
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/emotions')
def get_emotions():
    """Return available emotions"""
    return jsonify({'emotions': EMOTIONS})

@app.route('/status')
def get_status():
    """Return model status"""
    return jsonify({
        'model_loaded': emotion_model is not None,
        'emotions': EMOTIONS
    })

if __name__ == '__main__':
    print("=" * 50)
    print("Face Expression Detection System")
    print("=" * 50)
    
    # Load the emotion detection model
    load_emotion_model()
    
    if emotion_model is None:
        print("\n⚠ WARNING: Model not loaded. Emotion detection will not work.")
        print("Please ensure 'models/emotion_model.h5' exists.\n")
    
    print("\nStarting Flask application...")
    print("Access the app at: http://localhost:5000")
    print("Press Ctrl+C to stop")
    print("=" * 50)
    
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
