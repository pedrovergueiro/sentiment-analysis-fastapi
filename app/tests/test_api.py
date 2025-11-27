from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_sentiment_endpoint():
    # Se não houver internet / modelo disponível, aceita 503 Service Unavailable
    response = client.post("/sentiment/", json={"text": "I love Python!"})
    assert response.status_code in (200, 503)
    if response.status_code == 200:
        data = response.json()
        assert "label" in data
        assert "score" in data
