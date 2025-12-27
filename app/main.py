"""
🤖 Sentiment Analysis API - Aplicação Principal

Este é meu projeto de aprendizado sobre IA e NLP.
Aqui integro um modelo de Machine Learning com FastAPI.

Autor: Pedro Vergueiro
Objetivo: Aprender IA na prática
"""

from fastapi import FastAPI
from app.routers.sentiment import router as sentiment_router

# Criando a aplicação FastAPI com informações sobre IA
app = FastAPI(
    title="🤖 Sentiment Analysis API",
    description="API de análise de sentimentos usando IA - Projeto de aprendizado do Pedro Vergueiro",
    version="1.0.0",
    docs_url="/docs",  # Documentação interativa para testar a IA
    redoc_url="/redoc"  # Documentação alternativa
)

# Incluindo as rotas de análise de sentimentos (onde está a IA)
app.include_router(sentiment_router)

@app.get("/")
def home():
    """
    🏠 Página inicial da API
    
    Retorna informações básicas sobre a API de IA.
    Útil para verificar se o servidor está funcionando.
    """
    return {
        "message": "🤖 Sentiment Analysis API is running!",
        "creator": "Pedro Vergueiro",
        "purpose": "Aprender IA e NLP na prática",
        "docs": "/docs",
        "model": "HuggingFace Transformers"
    }
