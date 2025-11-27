from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from transformers import pipeline

router = APIRouter(prefix="/sentiment", tags=["Sentiment"])

# Carrega pipeline uma vez ao iniciar (pode demorar no primeiro download)
try:
    classifier = pipeline("sentiment-analysis")
except Exception as e:
    # Se estiver offline, falharemos com uma mensagem clara
    classifier = None

class TextInput(BaseModel):
    text: str

@router.post("/")
def analyze_sentiment(data: TextInput):
    if classifier is None:
        raise HTTPException(status_code=503, detail="Modelo não está disponível no servidor.")
    result = classifier(data.text)[0]
    return {
        "text": data.text,
        "label": result.get("label"),
        "score": float(result.get("score", 0.0))
    }
