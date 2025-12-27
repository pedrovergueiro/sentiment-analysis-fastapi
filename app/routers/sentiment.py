"""
🤖 Rotas de Análise de Sentimentos

Aqui está o coração da minha API de IA!
Este arquivo contém a lógica para analisar sentimentos usando Machine Learning.

O que aprendi implementando isso:
- Como carregar modelos de IA uma única vez (otimização)
- Como integrar HuggingFace Transformers com FastAPI
- Como tratar erros quando modelos não estão disponíveis
- Como estruturar respostas de APIs de IA
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from transformers import pipeline

# Criando o roteador para agrupar endpoints de IA
router = APIRouter(prefix="/sentiment", tags=["🤖 Análise de Sentimentos"])

# ========== CARREGAMENTO DO MODELO DE IA ==========
# IMPORTANTE: Carrego o modelo UMA VEZ quando a aplicação inicia
# Isso evita recarregar o modelo a cada requisição (seria muito lento!)
try:
    print("🤖 Carregando modelo de IA...")
    # Pipeline do HuggingFace para análise de sentimentos
    # Na primeira vez, vai baixar o modelo da internet (pode demorar)
    classifier = pipeline("sentiment-analysis")
    print("✅ Modelo de IA carregado com sucesso!")
except Exception as e:
    print(f"❌ Erro ao carregar modelo: {e}")
    # Se não conseguir carregar (sem internet, erro, etc.), define como None
    classifier = None

# ========== SCHEMAS DE DADOS ==========
class TextInput(BaseModel):
    """
    Schema para validar a entrada de texto.
    
    O Pydantic garante que sempre recebemos um texto válido.
    """
    text: str
    
    class Config:
        # Exemplo para a documentação automática
        schema_extra = {
            "example": {
                "text": "Eu amo programar em Python! É incrível!"
            }
        }

# ========== ENDPOINT PRINCIPAL DE IA ==========
@router.post("/")
def analyze_sentiment(data: TextInput):
    """
    🤖 Analisar sentimento de um texto usando IA
    
    Este é o endpoint principal onde a mágica da IA acontece!
    
    **Como funciona:**
    1. Recebo um texto em linguagem natural
    2. Passo o texto para o modelo de IA (Transformer)
    3. O modelo retorna POSITIVE ou NEGATIVE + score de confiança
    4. Retorno o resultado formatado
    
    **O que aprendi:**
    - Modelos de IA podem falhar (sem internet, erro de carregamento)
    - Sempre tratar erros graciosamente
    - Transformers retornam label + score
    - Score vai de 0 a 1 (confiança da predição)
    """
    
    # Verificar se o modelo está disponível
    if classifier is None:
        raise HTTPException(
            status_code=503, 
            detail="🚫 Modelo de IA não está disponível. Tente novamente mais tarde."
        )
    
    try:
        # AQUI ACONTECE A ANÁLISE DE IA! 🤖
        # O modelo processa o texto e retorna uma predição
        result = classifier(data.text)[0]
        
        # Formatando a resposta de forma clara
        return {
            "text": data.text,
            "label": result.get("label"),  # POSITIVE ou NEGATIVE
            "score": float(result.get("score", 0.0)),  # Confiança (0-1)
            "interpretation": {
                "sentiment": "Positivo" if result.get("label") == "POSITIVE" else "Negativo",
                "confidence": f"{float(result.get('score', 0.0)) * 100:.1f}%"
            }
        }
        
    except Exception as e:
        # Se algo der errado durante a análise
        raise HTTPException(
            status_code=500,
            detail=f"❌ Erro durante análise: {str(e)}"
        )

@router.get("/health")
def check_model_health():
    """
    🏥 Verificar se o modelo de IA está funcionando
    
    Endpoint útil para monitoramento e debugging.
    """
    if classifier is None:
        return {
            "status": "unhealthy",
            "model_loaded": False,
            "message": "Modelo não está carregado"
        }
    
    try:
        # Teste rápido com texto simples
        test_result = classifier("test")[0]
        return {
            "status": "healthy",
            "model_loaded": True,
            "message": "Modelo funcionando corretamente",
            "test_prediction": test_result
        }
    except Exception as e:
        return {
            "status": "unhealthy", 
            "model_loaded": True,
            "message": f"Modelo carregado mas com erro: {str(e)}"
        }
