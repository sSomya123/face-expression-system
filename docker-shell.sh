#!/bin/bash

# Face Expression Detection - Docker Commands
# ============================================

# 1. BUILD THE DOCKER IMAGE
# --------------------------
echo "Building Docker image..."
docker build -t face-expression-detector:latest .

# 2. RUN THE CONTAINER (Linux/WSL2 with webcam)
# ----------------------------------------------
echo "Running container with webcam access..."
docker run -d \
  --name face-expression-app \
  -p 5000:5000 \
  --device=/dev/video0:/dev/video0 \
  -v "$(pwd)/models:/app/models" \
  --restart unless-stopped \
  face-expression-detector:latest

# 3. RUN THE CONTAINER (Without webcam - for testing)
# ----------------------------------------------------
# docker run -d \
#   --name face-expression-app \
#   -p 5000:5000 \
#   -v "$(pwd)/models:/app/models" \
#   --restart unless-stopped \
#   face-expression-detector:latest

# 4. CHECK CONTAINER STATUS
# -------------------------
docker ps -a | grep face-expression-app

# 5. VIEW LOGS
# ------------
docker logs -f face-expression-app

# 6. STOP THE CONTAINER
# ---------------------
# docker stop face-expression-app

# 7. START THE CONTAINER
# ----------------------
# docker start face-expression-app

# 8. REMOVE THE CONTAINER
# -----------------------
# docker rm -f face-expression-app

# 9. REMOVE THE IMAGE
# -------------------
# docker rmi face-expression-detector:latest

# 10. REBUILD (after code changes)
# --------------------------------
# docker rm -f face-expression-app
# docker build -t face-expression-detector:latest .
# docker run -d --name face-expression-app -p 5000:5000 --device=/dev/video0:/dev/video0 face-expression-detector:latest

echo ""
echo "✅ Container is running!"
echo "🌐 Access the application at: http://localhost:5000"
echo ""
echo "Useful commands:"
echo "  - View logs: docker logs -f face-expression-app"
echo "  - Stop container: docker stop face-expression-app"
echo "  - Start container: docker start face-expression-app"
echo "  - Remove container: docker rm -f face-expression-app"
