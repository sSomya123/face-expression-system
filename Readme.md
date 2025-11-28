# Face Expression Detection System

A real-time face expression detection application using Deep Learning, OpenCV, and Flask with complete Docker integration.

## Features

- **Real-time Detection**: Detects 7 different emotions (Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral)
- **Web Interface**: Clean, modern UI for viewing live detection
- **Deep Learning**: CNN-based model for accurate emotion classification
- **Docker Ready**: Fully containerized for easy deployment
- **Confidence Scores**: Shows prediction confidence for each detection

## Project Structure

```
face-expression-detection/
├── app.py                  # Main Flask application
├── templates/
│   └── index.html         # Web interface
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose setup
├── requirements.txt       # Python dependencies
├── models/               # Model storage (created automatically)
└── README.md             # This file
```

## Installation & Setup

### Prerequisites

- Docker and Docker Compose installed
- Webcam connected to your system
- Linux/Mac/Windows with WSL2 for webcam support

### Option 1: Using Docker Compose (Recommended)

1. **Clone or create the project structure**:
```bash
mkdir face-expression-detection
cd face-expression-detection
```

2. **Create all necessary files** (app.py, Dockerfile, docker-compose.yml, requirements.txt, and templates/index.html)

3. **Build and run**:
```bash
docker-compose up --build
```

4. **Access the application**:
   Open your browser and navigate to `http://localhost:5000`

### Option 2: Using Docker Only

```bash
# Build the image
docker build -t face-expression-detector .

# Run the container
docker run -p 5000:5000 --device=/dev/video0:/dev/video0 face-expression-detector
```

### Option 3: Local Installation (Without Docker)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

## Usage

1. Start the application using one of the methods above
2. Open your web browser to `http://localhost:5000`
3. Allow camera access when prompted
4. The system will automatically detect faces and classify emotions in real-time
5. Emotions and confidence scores will be displayed on the video feed

## Technical Details

### Model Architecture

The application uses a Convolutional Neural Network with:
- 3 Convolutional layers (32, 64, 128 filters)
- MaxPooling layers for dimensionality reduction
- Dense layers with dropout for classification
- Softmax activation for 7-class emotion prediction

### Face Detection

- Uses OpenCV's Haar Cascade for face detection
- Processes images at 48x48 resolution
- Real-time processing with webcam feed

### Emotions Detected

1. Angry
2. Disgust
3. Fear
4. Happy
5. Sad
6. Surprise
7. Neutral

## Docker Configuration

### Dockerfile Features

- Based on Python 3.9 slim image
- Installs OpenCV dependencies
- Optimized for production deployment
- Minimal image size

### Docker Compose Features

- Automatic container restart
- Webcam device mapping
- Volume mounting for model persistence
- Port mapping for web access

## Troubleshooting

### Camera Not Working in Docker

**Linux**: Make sure your user has access to /dev/video0
```bash
sudo usermod -a -G video $USER
```

**Windows/Mac**: Docker Desktop may have limited webcam support. Consider running locally or using WSL2.

### Port Already in Use

Change the port mapping in docker-compose.yml:
```yaml
ports:
  - "8080:5000"  # Use port 8080 instead
```

### Model Not Loading

The application creates a basic model on first run. For better accuracy, you can train a custom model on the FER2013 dataset and place it in the project directory as `emotion_model.h5`.

## Customization

### Training Your Own Model

To train a custom model with better accuracy:

1. Download the FER2013 dataset
2. Modify the model architecture in app.py
3. Train using your dataset
4. Save the model as `emotion_model.h5`
5. Rebuild the Docker container

### Adjusting Detection Sensitivity

In `app.py`, modify the face detection parameters:
```python
faces = face_cascade.detectMultiScale(
    gray, 
    scaleFactor=1.1,  # Adjust this
    minNeighbors=5,   # And this
    minSize=(30, 30)  # Minimum face size
)
```

## Performance Optimization

- The model is loaded once at startup
- Frames are processed in real-time
- Face detection is optimized for speed
- Docker container uses minimal resources

## Future Enhancements

- [ ] Add support for multiple faces simultaneously
- [ ] Implement emotion history tracking
- [ ] Add REST API for integration
- [ ] Support for video file input
- [ ] Advanced model training pipeline
- [ ] Database integration for analytics

## License

This project is open-source and available for educational and commercial use.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## Support

For issues and questions, please open an issue on the project repository or contact the development team.
