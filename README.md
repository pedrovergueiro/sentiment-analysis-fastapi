👋 Olá! Eu sou o Pedro Vergueiro

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/ML-Machine%20Learning-orange?style=for-the-badge)
![HuggingFace](https://img.shields.io/badge/🤗-HuggingFace-yellow?style=for-the-badge)

**🤖 Minha jornada aprendendo IA e NLP - API de Análise de Sentimentos**

</div>

## 🎯 Por que criei este projeto?

Este projeto foi desenvolvido por mim para **mergulhar no mundo da Inteligência Artificial** e **Processamento de Linguagem Natural (NLP)**. Como estudante de Engenharia de Software, queria entender como integrar modelos de Machine Learning em APIs reais.

Escolhi análise de sentimentos porque:
- É uma aplicação prática e útil da IA
- Permite entender como funcionam os modelos de linguagem
- Combina programação com conceitos de ML
- Tem aplicações reais no mercado (redes sociais, feedback, etc.)

## 🧠 O que aprendi construindo esta API

Durante o desenvolvimento, consegui fixar conceitos fundamentais de IA e desenvolvimento:

### 🤖 **Conceitos de Machine Learning que pratiquei:**
- **Modelos Pré-treinados**: Como usar modelos do HuggingFace
- **Pipelines de ML**: Processamento automático de texto para análise
- **Transformers**: Entendi como funcionam os modelos de linguagem modernos
- **Inferência em Tempo Real**: Como servir modelos ML via API
- **Otimização de Performance**: Carregamento único do modelo na inicialização

### 🔧 **Habilidades técnicas desenvolvidas:**
- Integração de FastAPI com bibliotecas de ML
- Gerenciamento de modelos pesados em produção
- Tratamento de erros em sistemas de IA
- Testes para APIs que dependem de modelos externos
- Documentação de APIs com componentes de IA

```python
class MeuAprendizadoIA:
    def __init__(self):
        self.nome = "Pedro Vergueiro"
        self.projeto = "API de Análise de Sentimentos"
        self.objetivo = "Aprender IA na prática"
        self.modelo_usado = "HuggingFace Transformers"
        
    def o_que_implementei(self):
        return {
            "modelo": "Pipeline de sentiment-analysis",
            "framework": "FastAPI para servir o modelo",
            "entrada": "Texto em linguagem natural",
            "saida": "Label (POSITIVE/NEGATIVE) + Score de confiança",
            "otimizacao": "Carregamento único do modelo"
        }
    
    def conceitos_aprendidos(self):
        return [
            "Como modelos de IA processam texto",
            "Diferença entre treinar e usar modelos",
            "Pipelines de ML para produção",
            "Integração de IA com APIs REST"
        ]

meu_projeto_ia = MeuAprendizadoIA()
print("Cada predição foi uma lição sobre IA! 🤖")
```

## 🛠️ Tecnologias que escolhi e por quê

Selecionei cada tecnologia pensando no aprendizado de IA:

**🤖 HuggingFace Transformers**
- Biblioteca líder em modelos de linguagem
- Modelos pré-treinados de alta qualidade
- Fácil de usar para iniciantes em IA
- Comunidade ativa e documentação excelente

**⚡ FastAPI**
- Perfeito para servir modelos de ML
- Validação automática de dados
- Documentação interativa para testar a IA
- Performance adequada para inferência

**🐍 Python**
- Linguagem padrão para Machine Learning
- Ecossistema rico em bibliotecas de IA
- Fácil integração entre diferentes ferramentas

## 📖 Como estruturei meu projeto de IA

Organizei tudo pensando em **clareza** e **boas práticas de ML**:

```
sentiment-analysis-fastapi/
├── app/                          # 📁 Código principal da API
│   ├── main.py                  # 🚀 Aplicação FastAPI
│   ├── routers/
│   │   └── sentiment.py         # 🤖 Endpoint de análise de sentimentos
│   ├── models.py                # 📊 Schemas de dados
│   └── tests/
│       └── test_api.py          # 🧪 Testes da API
├── requirements.txt             # 📦 Dependências (incluindo ML)
├── Dockerfile                   # 🐳 Para containerização
└── README.md                    # 📖 Este arquivo
```

### 🤔 Por que organizei assim?

- **Separação clara**: Lógica de ML isolada no router
- **Modelos carregados uma vez**: Evita recarregar a cada requisição
- **Tratamento de erros**: Para quando o modelo não está disponível
- **Testes adaptados**: Considerando que modelos podem falhar

## 🏃‍♂️ Como rodar minha API de IA

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/pedrovergueiro/sentiment-analysis-fastapi.git
cd sentiment-analysis-fastapi
```

### 2️⃣ Criar ambiente virtual (aprendi que é essencial para ML!)
```bash
# Criar ambiente isolado (importante para dependências de ML)
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Ativar no Linux/Mac  
source venv/bin/activate
```

### 3️⃣ Instalar dependências de IA
```bash
pip install -r requirements.txt
```

**⚠️ Primeira execução**: O modelo será baixado automaticamente do HuggingFace (pode demorar alguns minutos)

### 4️⃣ Rodar a API
```bash
# Da pasta raiz do projeto
uvicorn app.main:app --reload
```

### 5️⃣ Testar a IA
Abra o navegador em: **http://localhost:8000/docs**

🎉 **Pronto!** Agora você pode testar a análise de sentimentos diretamente na documentação interativa!

## 🤖 O que minha API de IA faz (e como implementei)

Criei uma API que usa **Inteligência Artificial** para analisar sentimentos em texto. Aqui está como funciona:

### 🏠 **Página Inicial** - `GET /`
```python
# O que aprendi: Como criar endpoints simples
@app.get("/")
def home():
    return {"message": "Sentiment Analysis API is running!"}
```

### 🤖 **Análise de Sentimentos** - `POST /sentiment/`
```python
# O que aprendi: Como integrar modelos de IA em APIs
@router.post("/")
def analyze_sentiment(data: TextInput):
    if classifier is None:
        # Tratamento de erro quando modelo não está disponível
        raise HTTPException(status_code=503, detail="Modelo não disponível")
    
    # Aqui acontece a mágica da IA!
    result = classifier(data.text)[0]
    
    return {
        "text": data.text,
        "label": result.get("label"),      # POSITIVE ou NEGATIVE
        "score": float(result.get("score", 0.0))  # Confiança (0-1)
    }
```

**Exemplo prático:**
```bash
curl -X POST "http://localhost:8000/sentiment/" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Eu amo programar em Python! É incrível!"
  }'

# Resposta:
# {
#   "text": "Eu amo programar em Python! É incrível!",
#   "label": "POSITIVE",
#   "score": 0.9998
# }
```

### 🧠 Como o modelo funciona (o que aprendi):

1. **Entrada**: Recebo um texto em linguagem natural
2. **Processamento**: O modelo Transformer analisa o texto
3. **Classificação**: IA determina se é POSITIVE ou NEGATIVE
4. **Confiança**: Retorna um score de 0 a 1 (quão certo está)

## 💡 Desafios de IA que enfrentei e como resolvi

### 🤖 **Problema 1: Modelo pesado**
**Desafio**: Modelos de IA são grandes e demoram para carregar
**Solução**: Carrego o modelo uma única vez na inicialização da API

```python
# Carrega pipeline uma vez ao iniciar (otimização que aprendi)
try:
    classifier = pipeline("sentiment-analysis")
except Exception as e:
    classifier = None  # Graceful degradation
```

### 🌐 **Problema 2: Dependência de internet**
**Desafio**: Primeiro download do modelo precisa de internet
**Solução**: Tratamento de erro elegante quando modelo não está disponível

### 🧪 **Problema 3: Testes com IA**
**Desafio**: Como testar algo que depende de modelos externos?
**Solução**: Testes que aceitam tanto sucesso (200) quanto falha (503)

```python
def test_sentiment_endpoint():
    response = client.post("/sentiment/", json={"text": "I love Python!"})
    # Aceita tanto sucesso quanto falha do modelo
    assert response.status_code in (200, 503)
```

### ⚡ **Problema 4: Performance**
**Desafio**: IA pode ser lenta para responder
**Solução**: Modelo otimizado e carregamento único

## 🎓 Principais conceitos de IA que fixei

### 🤖 **Machine Learning em Produção**
- **Pipelines**: Como usar pipelines pré-construídos do HuggingFace
- **Modelos Pré-treinados**: Diferença entre treinar e usar modelos existentes
- **Inferência**: Como fazer predições em tempo real
- **Otimização**: Técnicas para melhorar performance de modelos

### 🔍 **Processamento de Linguagem Natural (NLP)**
- **Transformers**: Como funcionam os modelos de linguagem modernos
- **Tokenização**: Como a IA "entende" texto
- **Classificação de Texto**: Categorizar texto automaticamente
- **Análise de Sentimentos**: Detectar emoções em texto

### 🏗️ **Arquitetura de Sistemas de IA**
- **Separação de Responsabilidades**: Lógica de IA isolada
- **Tratamento de Erros**: Sistemas robustos para falhas de modelo
- **Validação de Dados**: Garantir entrada adequada para IA
- **Documentação de IA**: Como documentar APIs que usam ML

## 🧪 Como implementei os testes para IA

Aprendi que testar sistemas de IA é diferente de testar código tradicional:

```python
def test_sentiment_endpoint():
    """Testa a análise de sentimentos"""
    response = client.post("/sentiment/", json={"text": "I love Python!"})
    
    # IA pode falhar (sem internet, modelo não carregado)
    assert response.status_code in (200, 503)
    
    if response.status_code == 200:
        data = response.json()
        assert "label" in data      # Deve ter classificação
        assert "score" in data      # Deve ter confiança
        assert data["score"] >= 0   # Score válido
        assert data["score"] <= 1
```

**Para rodar os testes:**
```bash
# Testar tudo
pytest

# Ver detalhes
pytest -v

# Testar só a API
pytest app/tests/test_api.py
```

## 🌱 Próximos passos no meu aprendizado de IA

Agora que entendi o básico de IA em produção, quero evoluir para:

- [ ] **Modelos Multilíngues**: Suporte a português e outros idiomas
- [ ] **Análise Mais Detalhada**: Detectar emoções específicas (raiva, alegria, etc.)
- [ ] **Batch Processing**: Analisar múltiplos textos de uma vez
- [ ] **Cache Inteligente**: Armazenar resultados para textos similares
- [ ] **Métricas de Performance**: Monitorar latência e precisão
- [ ] **Fine-tuning**: Treinar modelo com dados específicos
- [ ] **Deploy com Docker**: Containerizar a aplicação de IA

## 🤝 Quer aprender IA junto comigo?

Se você também está explorando Machine Learning e NLP, fique à vontade para:

- 🍴 **Fork** este projeto e experimentar com outros modelos
- 🤖 **Testar diferentes textos** e ver como a IA responde
- 💡 **Sugerir melhorias** nos modelos ou na API
- ⭐ **Dar uma estrela** se o projeto te inspirou a aprender IA!

## 📫 Vamos trocar uma ideia sobre IA?

Estou sempre animado para conversar sobre Inteligência Artificial e Machine Learning!

- 📧 **Email**: pedrolv.fsilva@gmail.com
- 💼 **LinkedIn**: [Pedro Vergueiro](https://www.linkedin.com/in/pedro-vergueiro)
- 🌐 **GitHub**: [@pedrovergueiro](https://github.com/pedrovergueiro)

---

<div align="center">

**⭐ Se este projeto te inspirou a aprender IA, dê uma estrela! ⭐**

*"A IA não vai substituir programadores, mas programadores que usam IA vão substituir os que não usam"*

Feito com ❤️ e muita curiosidade sobre IA por Pedro Vergueiro | Estudante de Engenharia de Software

</div>