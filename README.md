<div align="center">🧠 SentimentFlow
API Inteligente de Análise de Sentimento com FastAPI + Transformers + PyTorch
</div> <p align="center"> <img src="https://img.shields.io/badge/python-3.11-blue?style=for-the-badge"> <img src="https://img.shields.io/badge/FastAPI-Performance%20First-009688?style=for-the-badge"> <img src="https://img.shields.io/badge/HuggingFace-Transformers-ffcc4d?style=for-the-badge"> <img src="https://img.shields.io/badge/PyTorch-Deep%20Learning-ee4c2c?style=for-the-badge"> <img src="https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=for-the-badge"> </p>
✨ Visão Geral

SentimentFlow é uma API moderna e escalável de análise de sentimento construída com:

⚡ FastAPI (altíssima performance e documentação automática)

🤗 Transformers (modelos pré-treinados da HuggingFace)

🔥 PyTorch (engine de deep learning)

Ela recebe um texto e retorna:

✔ POSITIVE
✔ NEGATIVE
✔ NEUTRAL
✔ Com score de confiança

Além disso, foi construída seguindo boas práticas de arquitetura, ideal para demonstrar habilidades reais em backend Python — perfeita para colocar no portfólio e impressionar recrutadores.

🎯 Por que este projeto é indispensável no portfólio?

Ele demonstra domínio de:

🟩 Backend Profissional

Rotas assíncronas

Validação segura com Pydantic

Uso de boas práticas (tipagem, versionamento de API, previsibilidade)

🟦 Machine Learning aplicado

Uso de modelos Transformers

Inferência otimizada

Pipeline real de NLP

🟧 Ferramentas de Produção

Dockerfile otimizado

Uvicorn ASGI server

Testes automatizados com pytest

Estrutura limpa (app/ modules)

🟪 Documentação Moderna

Swagger / OpenAPI

ReDoc


🏗️ Arquitetura da Aplicação
Cliente -> FastAPI -> Pipeline Transformers -> Modelo HuggingFace -> Resposta JSON

Diagrama
                          ┌─────────────────────────┐
                          │        Cliente           │
                          │  (Front / App / cURL)    │
                          └─────────────┬───────────┘
                                        │ POST /predict
                                        ▼
                         ┌──────────────────────────────┐
                         │            FastAPI            │
                         │  Rotas / Validação / Schema   │
                         └──────────────┬───────────────┘
                                        │ envia texto
                                        ▼
                         ┌──────────────────────────────┐
                         │     Transformers Pipeline     │
                         └──────────────┬───────────────┘
                                        │ processa
                                        ▼
                         ┌──────────────────────────────┐
                         │ Modelo pré-treinado BERT/SST2 │
                         └──────────────────────────────┘
                                        │ retorna label + score
                                        ▼
                         ┌──────────────────────────────┐
                         │         JSON Response         │
                         └──────────────────────────────┘

📁 Estrutura do Projeto
sentimentflow/
│── app/
│   ├── main.py        # Inicialização da API
│   ├── model.py       # Carregamento do modelo Transformers
│   ├── schemas.py     # Pydantic models
│   └── utils.py       # Funções auxiliares
│── tests/
│   └── test_sentiment.py
│── Dockerfile
│── requirements.txt
│── README.md

▶️ Como Rodar Localmente
1️⃣ Clone o repositório
git clone https://github.com/SEU_USUARIO/sentimentflow.git
cd sentimentflow

2️⃣ Crie e ative o venv
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Linux/Mac

3️⃣ Instale dependências
pip install -r requirements.txt

4️⃣ Rode o servidor
uvicorn app.main:app --reload

🌐 Acessar a Documentação
Tipo	URL
Swagger UI	http://localhost:8000/docs

ReDoc	http://localhost:8000/redoc

Healthcheck	http://localhost:8000/
🧪 Testes
pytest -v

📦 Deploy com Docker
docker build -t sentimentflow .
docker run -p 8000:8000 sentimentflow

💡 Exemplo de Uso (cURL)
curl -X POST http://localhost:8000/predict \
    -H "Content-Type: application/json" \
    -d "{\"text\": \"I love this project!\"}"

    📬 Futuras melhorias

Adicionar histórico de análises (banco de dados SQLModel)

Dashboard em React consumindo a API

Suporte a múltiplos idiomas

Versionamento de modelos

Deploy em cloud (Railway, Render, AWS ou GCP)

🔮 Roadmap

 Suporte a múltiplos idiomas

 Cache de inferência

 Logging estruturado

 Ajuste fino de modelo custom

 Metrics + Prometheus

 Deploy automático (CI/CD)

🧑‍💻 Autor

Pedro Lucas
Desenvolvedor Python — APIs | IA | Automação

⭐ Gostou do projeto?

Deixe uma estrela no repositório ⭐
Isso ajuda MUITO no portfólio!