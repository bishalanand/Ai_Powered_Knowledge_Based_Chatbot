#!/bin/bash

# RAG Chatbot Deployment Script

set -e

echo "🚀 Starting RAG Chatbot deployment..."

# Check if .env file exists
if [ ! -f .env ]; then
    echo "❌ .env file not found. Please copy .env.example to .env and fill in your API keys."
    exit 1
fi

# Create data directory if it doesn't exist
mkdir -p data/uploads

# Stop and remove existing containers
echo "🛑 Stopping existing containers..."
docker-compose down || true

# Build and start services
echo "🏗️ Building and starting services..."
docker-compose up --build -d

# Wait for services to be healthy
echo "⏳ Waiting for services to start..."
sleep 10

# Check if backend is responding
echo "🔍 Checking backend health..."
if curl -f http://localhost/api/docs > /dev/null 2>&1; then
    echo "✅ Backend is healthy"
else
    echo "❌ Backend health check failed"
    docker-compose logs backend
    exit 1
fi

# Check if frontend is responding
echo "🔍 Checking frontend..."
if curl -f http://localhost > /dev/null 2>&1; then
    echo "✅ Frontend is responding"
else
    echo "❌ Frontend check failed"
    docker-compose logs frontend
    exit 1
fi

echo "🎉 Deployment completed successfully!"
echo "🌐 Frontend: http://localhost"
echo "📚 API Docs: http://localhost/api/docs"
echo ""
echo "To view logs: docker-compose logs -f"
echo "To stop: docker-compose down"