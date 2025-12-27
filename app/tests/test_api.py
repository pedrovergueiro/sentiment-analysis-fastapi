"""
🧪 Testes da API de Análise de Sentimentos

Aqui testo se minha API de IA está funcionando corretamente.
Testar IA é diferente de testar código normal!

O que aprendi sobre testes de IA:
- Modelos podem falhar (sem internet, erro de carregamento)
- Preciso testar tanto sucesso quanto falha
- Resultados de IA podem variar, então testo estrutura da resposta
- Importante testar casos extremos (texto vazio, muito longo, etc.)
"""

from fastapi.testclient import TestClient
from app.main import app

# Cliente de teste para fazer requisições à API
client = TestClient(app)

def test_home():
    """
    🏠 Testa se a página inicial funciona
    """
    response = client.get("/")
    assert response.status_code == 200
    
    data = response.json()
    assert "message" in data
    assert "creator" in data
    assert data["creator"] == "Pedro Vergueiro"

def test_sentiment_endpoint_success():
    """
    🤖 Testa análise de sentimentos com texto positivo
    
    Nota: Este teste pode falhar se o modelo não estiver disponível,
    e isso é esperado! IA depende de recursos externos.
    """
    test_text = "I love Python programming! It's amazing!"
    
    response = client.post("/sentiment/", json={"text": test_text})
    
    # Aceita tanto sucesso (200) quanto falha do modelo (503)
    assert response.status_code in (200, 503)
    
    if response.status_code == 200:
        data = response.json()
        
        # Verifica estrutura da resposta de IA
        assert "text" in data
        assert "label" in data
        assert "score" in data
        assert "interpretation" in data
        
        # Verifica se o texto original foi preservado
        assert data["text"] == test_text
        
        # Verifica se o label é válido
        assert data["label"] in ["POSITIVE", "NEGATIVE"]
        
        # Verifica se o score está no range correto
        assert 0.0 <= data["score"] <= 1.0
        
        # Verifica interpretação em português
        assert "sentiment" in data["interpretation"]
        assert "confidence" in data["interpretation"]

def test_sentiment_endpoint_negative():
    """
    🤖 Testa análise de sentimentos com texto negativo
    """
    test_text = "I hate bugs in my code. This is terrible!"
    
    response = client.post("/sentiment/", json={"text": test_text})
    
    # Aceita tanto sucesso quanto falha
    assert response.status_code in (200, 503)
    
    if response.status_code == 200:
        data = response.json()
        assert data["text"] == test_text
        assert data["label"] in ["POSITIVE", "NEGATIVE"]

def test_sentiment_validation_error():
    """
    ❌ Testa validação de dados inválidos
    
    A API deve rejeitar textos vazios ou inválidos.
    """
    # Teste com texto vazio
    response = client.post("/sentiment/", json={"text": ""})
    assert response.status_code == 422  # Validation Error
    
    # Teste sem campo text
    response = client.post("/sentiment/", json={})
    assert response.status_code == 422  # Validation Error

def test_sentiment_very_long_text():
    """
    📏 Testa com texto muito longo
    
    Verifica se a API lida bem com textos grandes.
    """
    # Texto muito longo (mais de 5000 caracteres)
    long_text = "This is a test. " * 400  # ~6400 caracteres
    
    response = client.post("/sentiment/", json={"text": long_text})
    
    # Deve dar erro de validação (texto muito longo)
    assert response.status_code == 422

def test_model_health_endpoint():
    """
    🏥 Testa endpoint de saúde do modelo
    
    Verifica se conseguimos monitorar o status da IA.
    """
    response = client.get("/sentiment/health")
    assert response.status_code == 200
    
    data = response.json()
    assert "status" in data
    assert "model_loaded" in data
    assert "message" in data
    
    # Status deve ser healthy ou unhealthy
    assert data["status"] in ["healthy", "unhealthy"]
    
    # model_loaded deve ser boolean
    assert isinstance(data["model_loaded"], bool)

def test_sentiment_portuguese_text():
    """
    🇧🇷 Testa com texto em português
    
    Verifica se o modelo funciona com outros idiomas.
    """
    test_text = "Eu amo programar em Python! É incrível!"
    
    response = client.post("/sentiment/", json={"text": test_text})
    
    # Aceita tanto sucesso quanto falha
    assert response.status_code in (200, 503)
    
    if response.status_code == 200:
        data = response.json()
        assert data["text"] == test_text
        # Modelo pode ou não funcionar bem com português
        # Mas deve retornar estrutura válida
        assert "label" in data
        assert "score" in data

def test_sentiment_mixed_content():
    """
    🔀 Testa com conteúdo misto (emojis, números, etc.)
    """
    test_text = "Python is great! 🐍 I rate it 10/10 ⭐⭐⭐"
    
    response = client.post("/sentiment/", json={"text": test_text})
    
    assert response.status_code in (200, 503)
    
    if response.status_code == 200:
        data = response.json()
        assert data["text"] == test_text
        assert "label" in data
