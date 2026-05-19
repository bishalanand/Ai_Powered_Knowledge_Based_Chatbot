from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.upload import router as upload_router
from api.summary import router as summary_router
from api.chat import router as chat_router

app = FastAPI(
    title="AI PDF Chatbot API",
    description="Backend for PDF based RAG chatbot",
    version="1.0"
)

# Allowed frontend URLs
origins = [
    "http://localhost:5173",  # React local
    "http://127.0.0.1:5173",

    # Add Vercel URL after deployment
    # "https://your-app.vercel.app"
]

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(upload_router)
app.include_router(summary_router)
app.include_router(chat_router)


@app.get("/")
def home():
    return {"message": "Backend running successfully"}