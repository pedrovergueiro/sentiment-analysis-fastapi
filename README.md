# Sentiment Analysis API - FastAPI

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/ML-Machine%20Learning-orange?style=for-the-badge)
![NLP](https://img.shields.io/badge/NLP-Natural%20Language%20Processing-blue?style=for-the-badge)

**API de Análise de Sentimentos com Machine Learning | FastAPI | NLP | Processamento de Texto**

</div>

---

## 📋 Sobre o Projeto

API REST desenvolvida com **FastAPI** para análise de sentimentos utilizando técnicas de **Machine Learning** e **Processamento de Linguagem Natural (NLP)**. O sistema processa texto em tempo real e retorna análises de sentimento com alta precisão.

### 🎯 Objetivo

Criar uma API production-ready que demonstre integração de modelos de Machine Learning em APIs REST, processamento de texto avançado e otimização de performance para análise em tempo real.

---

## 🚀 Tecnologias

### Core
- **Python 3.8+** - Linguagem principal
- **FastAPI** - Framework web moderno e rápido
- **NLTK** - Processamento de linguagem natural
- **TextBlob** - Análise de sentimentos
- **Scikit-learn** - Machine Learning

### Processamento de Texto
- **spaCy** - NLP avançado
- **Transformers** - Modelos pré-treinados
- **WordCloud** - Visualização de dados

### Infraestrutura
- **Docker** - Containerização
- **Redis** - Cache de resultados
- **PostgreSQL** - Armazenamento de histórico

---

## 📊 Features Principais

### 🧠 Análise de Sentimentos
- ✅ Análise em tempo real com baixa latência
- ✅ Suporte a múltiplos idiomas
- ✅ Classificação: Positivo, Negativo, Neutro
- ✅ Score de confiança para cada análise

### 📝 Processamento de Texto
- ✅ Tokenização e limpeza de texto
- ✅ Remoção de stopwords
- ✅ Stemming e lemmatization
- ✅ Análise de entidades nomeadas

### ⚡ Performance
- ✅ Cache de resultados frequentes
- ✅ Processamento assíncrono
- ✅ Otimização de modelos ML
- ✅ Resposta média < 100ms

### 📚 Documentação
- ✅ Documentação automática Swagger/OpenAPI
- ✅ Exemplos de uso
- ✅ Schema de dados completo

---

## 💻 Instalação

### Pré-requisitos

```bash
Python 3.8 ou superior
pip (gerenciador de pacotes Python)
```

### Instalação

```bash
# Clone o repositório
git clone https://github.com/pedrovergueiro/sentiment-analysis-fastapi.git
cd sentiment-analysis-fastapi

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Baixe os modelos NLP necessários
python -m nltk.downloader all
python -m spacy download en_core_web_sm

# Inicie o servidor
uvicorn main:app --reload
```

---

## 🏗️ Arquitetura

```
sentiment-analysis-fastapi/
├── app/
│   ├── api/
│   │   └── routes/
│   │       └── sentiment.py  # Rotas de análise
│   ├── core/
│   │   ├── config.py          # Configurações
│   │   └── ml_models.py       # Modelos ML
│   ├── services/
│   │   ├── text_processor.py  # Processamento de texto
│   │   └── sentiment_analyzer.py  # Análise de sentimentos
│   ├── schemas/
│   │   └── sentiment.py       # Schemas Pydantic
│   └── main.py                 # Aplicação principal
├── models/                     # Modelos ML treinados
├── tests/                      # Testes automatizados
├── requirements.txt
└── README.md
```

---

## 📡 Endpoints Principais

### Análise de Sentimentos
- `POST /api/sentiment/analyze` - Analisar sentimento de texto
- `POST /api/sentiment/batch` - Análise em lote
- `GET /api/sentiment/history` - Histórico de análises

### Exemplo de Requisição

```python
import requests

response = requests.post("http://localhost:8000/api/sentiment/analyze", json={
    "text": "Este produto é incrível! Estou muito satisfeito.",
    "language": "pt"
})

result = response.json()
# {
#   "sentiment": "positive",
#   "confidence": 0.95,
#   "score": 0.87
# }
```

---

## 🧪 Modelos de Machine Learning

### Modelos Implementados
- **TextBlob** - Análise básica de sentimentos
- **VADER** - Análise específica para redes sociais
- **BERT** - Modelo transformer pré-treinado (opcional)
- **Custom Model** - Modelo treinado com dados específicos

### Performance dos Modelos
- TextBlob: ~50ms por análise
- VADER: ~30ms por análise
- BERT: ~200ms por análise (maior precisão)

---

## 📈 Casos de Uso

### Análise de Feedback de Clientes
```python
feedback = "O atendimento foi excelente, mas o produto demorou a chegar"
result = analyze_sentiment(feedback)
# Retorna análise detalhada do feedback
```

### Monitoramento de Redes Sociais
```python
tweets = ["Tweet 1", "Tweet 2", "Tweet 3"]
results = batch_analyze(tweets)
# Análise em lote para múltiplos textos
```

### Análise de Reviews
```python
reviews = load_reviews_from_database()
sentiments = analyze_batch(reviews)
# Processamento de grandes volumes de dados
```

---

## ⚡ Otimizações

- ✅ Cache Redis para textos frequentes
- ✅ Processamento assíncrono com asyncio
- ✅ Batch processing para múltiplos textos
- ✅ Modelos otimizados para produção
- ✅ Compressão de modelos ML

---

## 🔒 Segurança

- ✅ Validação de entrada de dados
- ✅ Rate limiting para prevenir abuso
- ✅ Sanitização de texto de entrada
- ✅ Proteção contra injection attacks

---

## 📚 Documentação da API

Após iniciar o servidor, acesse:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 🧪 Testes

```bash
# Executar todos os testes
pytest

# Executar testes específicos
pytest tests/test_sentiment.py

# Teste de performance
pytest tests/test_performance.py
```

---

## 📊 Métricas de Performance

- ✅ Latência média: < 100ms
- ✅ Throughput: > 100 requisições/segundo
- ✅ Precisão do modelo: > 85%
- ✅ Suporte a textos de até 5000 caracteres

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

---

## 📝 Licença

Este projeto está sob a licença MIT.

---

## 👨‍💻 Desenvolvedor

**Pedro L. Vergueiro**

- 📧 Email: pedrolv.fsilva@gmail.com
- 💼 LinkedIn: [Pedro L. Vergueiro](https://www.linkedin.com/in/pedro-vergueiro)
- 🌐 GitHub: [@pedrovergueiro](https://github.com/pedrovergueiro)

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela! ⭐**

Made with ❤️ by Pedro L. Vergueiro

</div>
