# API de Análise de Sentimentos

Meu primeiro projeto unindo machine learning com uma API que outras pessoas poderiam consumir. A ideia era: você manda um texto, a API te diz se o sentimento é positivo, negativo ou neutro.

O modelo em si é básico — não é nenhum BERT finado — mas o desafio maior foi estruturar o projeto de forma que ele fosse de fato utilizável: Docker pra não ter problema de "na minha máquina funciona", CI com GitHub Actions pra rodar os testes automaticamente a cada push, e uma documentação que explica como usar sem precisar ler o código.

```bash
# Testar em 30 segundos
docker-compose up
curl -X POST http://localhost:8000/analyze   -H "Content-Type: application/json"   -d '{"text": "Esse projeto foi divertido de fazer"}'
```

## Stack
Python · FastAPI · Docker · GitHub Actions · pytest
