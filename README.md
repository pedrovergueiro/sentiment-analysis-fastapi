# API de Análise de Sentimentos

Esse foi o projeto onde tentei unir pela primeira vez machine learning com desenvolvimento de APIs. A ideia era simples: receber um texto e devolver se o sentimento era positivo, negativo ou neutro.

Aprendi bastante sobre como servir um modelo de ML via API REST e, de quebra, como estruturar melhor um projeto Python — separando responsabilidades, escrevendo testes e até containerizando com Docker.

Ainda tem muita coisa que eu melhoraria hoje (a análise de sentimentos em si ainda é bem básica), mas foi um projeto importante pra minha evolução.

## O que aprendi
- Integrar NLP com uma API REST usando FastAPI
- Como o Docker facilita o deploy de projetos com dependências pesadas
- Boas práticas de estrutura de projeto Python
- Escrever testes básicos com pytest

## Como rodar

```bash
# Com Docker
docker-compose up

# Sem Docker
pip install -r requirements.txt
python run.py
```

## Stack
Python · FastAPI · Docker · NLP · pytest · GitHub Actions
