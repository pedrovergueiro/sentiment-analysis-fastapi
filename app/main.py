from fastapi import FastAPI
from app.routers.sentiment import router as sentiment_router

app = FastAPI(
    title="Sentiment Analysis API",
    description="API de análise de sentimento usando HuggingFace",
    version="1.0.0"
)

app.include_router(sentiment_router)

@app.get("/")
def home():
    return {"message": "Sentiment Analysis API is running!"}
