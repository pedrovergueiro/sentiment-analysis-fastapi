"""
📊 Modelos de Dados para IA

Aqui defino como os dados são estruturados na minha API de IA.
Uso Pydantic para validação automática e documentação.

O que aprendi sobre schemas para IA:
- Validação é crucial para modelos de ML (garbage in, garbage out)
- Documentação clara ajuda outros desenvolvedores
- Exemplos facilitam o teste da API
"""

from pydantic import BaseModel, Field
from typing import Optional

class TextInput(BaseModel):
    """
    Schema para entrada de texto na análise de sentimentos.
    
    Garante que sempre recebemos um texto válido para a IA processar.
    """
    text: str = Field(
        min_length=1,
        max_length=5000,
        description="Texto para análise de sentimentos",
        example="Eu amo programar em Python! É incrível!"
    )

class SentimentResult(BaseModel):
    """
    Schema para resultado da análise de sentimentos.
    
    Define o formato padronizado de resposta da IA.
    """
    text: str = Field(description="Texto original analisado")
    label: str = Field(description="Classificação: POSITIVE ou NEGATIVE")
    score: float = Field(
        ge=0.0, 
        le=1.0, 
        description="Confiança da predição (0-1)"
    )
    interpretation: Optional[dict] = Field(
        description="Interpretação em português",
        example={
            "sentiment": "Positivo",
            "confidence": "99.8%"
        }
    )

class ModelHealth(BaseModel):
    """
    Schema para status de saúde do modelo de IA.
    
    Útil para monitoramento e debugging.
    """
    status: str = Field(description="healthy ou unhealthy")
    model_loaded: bool = Field(description="Se o modelo está carregado")
    message: str = Field(description="Detalhes do status")
    test_prediction: Optional[dict] = Field(description="Teste de predição")
