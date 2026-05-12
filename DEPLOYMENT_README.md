# RAG Chatbot Production Deployment

This guide explains how to deploy the RAG-based PDF chatbot application in production using Docker.

## Prerequisites

- Docker and Docker Compose installed
- Pinecone account and API key
- Groq API key

## Quick Deployment

1. **Clone and setup environment:**
   ```bash
   git clone <your-repo>
   cd faq-project
   cp .env.example .env
   ```

2. **Configure environment variables:**
   Edit `.env` file with your actual API keys:
   ```
   PINECONE_API_KEY=your_actual_pinecone_key
   GROQ_API_KEY=your_actual_groq_key
   ```

3. **Deploy:**
   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```

## Manual Deployment

If you prefer manual control:

```bash
# Build and start services
docker-compose up --build -d

# Check logs
docker-compose logs -f

# Stop services
docker-compose down
```

## Architecture

- **Frontend**: React app served by Nginx (port 80)
- **Backend**: FastAPI application (port 8000, proxied through Nginx)
- **Data**: Persistent volume for uploaded files

## API Endpoints

- Frontend: `http://localhost`
- API Documentation: `http://localhost/api/docs`
- Health Check: `http://localhost/health`

## Production Considerations

1. **Security**:
   - Change default ports if needed
   - Use HTTPS in production (add SSL certificates)
   - Secure API keys properly

2. **Scaling**:
   - Add load balancer for multiple instances
   - Use Redis for session/caching if needed
   - Consider using managed databases for vector storage

3. **Monitoring**:
   - Add logging aggregation
   - Set up health checks and alerts
   - Monitor resource usage

## Troubleshooting

- Check logs: `docker-compose logs <service-name>`
- Restart services: `docker-compose restart`
- Rebuild: `docker-compose up --build --force-recreate`

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| PINECONE_API_KEY | Pinecone vector database API key | Yes |
| PINECONE_INDEX_NAME | Pinecone index name | Yes |
| GROQ_API_KEY | Groq LLM API key | Yes |