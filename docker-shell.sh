#!/bin/bash

# Docker Compose Commands for Face Expression Detection
# ======================================================

echo "Face Expression Detection - Docker Compose Commands"
echo "===================================================="
echo ""

# 1. BUILD AND START (First Time)
echo "1. Build and start the application:"
echo "   docker-compose up --build"
echo ""

# 2. START IN BACKGROUND
echo "2. Start in detached mode (background):"
echo "   docker-compose up -d"
echo ""

# 3. START WITH BUILD
echo "3. Rebuild and start:"
echo "   docker-compose up --build -d"
echo ""

# 4. VIEW LOGS
echo "4. View logs:"
echo "   docker-compose logs -f"
echo "   docker-compose logs -f face-expression-detector"
echo ""

# 5. STOP SERVICES
echo "5. Stop services:"
echo "   docker-compose stop"
echo ""

# 6. START SERVICES
echo "6. Start services (after stop):"
echo "   docker-compose start"
echo ""

# 7. RESTART SERVICES
echo "7. Restart services:"
echo "   docker-compose restart"
echo ""

# 8. STOP AND REMOVE CONTAINERS
echo "8. Stop and remove containers:"
echo "   docker-compose down"
echo ""

# 9. STOP, REMOVE CONTAINERS AND VOLUMES
echo "9. Stop, remove containers and volumes:"
echo "   docker-compose down -v"
echo ""

# 10. VIEW RUNNING SERVICES
echo "10. View running services:"
echo "    docker-compose ps"
echo ""

# 11. EXECUTE COMMAND IN CONTAINER
echo "11. Execute command in container:"
echo "    docker-compose exec face-expression-detector bash"
echo ""

# 12. VIEW SERVICE STATUS
echo "12. Check service health:"
echo "    docker-compose ps"
echo "    docker inspect face_expression_app"
echo ""

# 13. REBUILD WITHOUT CACHE
echo "13. Rebuild without cache:"
echo "    docker-compose build --no-cache"
echo "    docker-compose up -d"
echo ""

# 14. SCALE SERVICES (if needed)
echo "14. Scale services:"
echo "    docker-compose up -d --scale face-expression-detector=2"
echo ""

echo "===================================================="
echo "Quick Start:"
echo "  docker-compose up --build -d"
echo "  docker-compose logs -f"
echo ""
echo "Access: http://localhost:5000"
echo "===================================================="
