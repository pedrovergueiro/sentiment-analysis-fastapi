# 🚀 Como Usar a Sentiment Analysis API

## ✅ Guia Rápido

Esta API usa **Inteligência Artificial** para analisar sentimentos em texto. É perfeita para aprender sobre IA na prática!

### 🏃‍♂️ Para Rodar a API

```bash
# 1. Clone o repositório
git clone https://github.com/pedrovergueiro/sentiment-analysis-fastapi.git
cd sentiment-analysis-fastapi

# 2. Crie ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac

# 3. Instale dependências
pip install -r requirements.txt

# 4. Inicie a API
uvicorn app.main:app --reload
```

### 🌐 Acessar a API

- **Documentação**: http://localhost:8000/docs
- **API**: http://localhost:8000/
- **Status da IA**: http://localhost:8000/sentiment/health

## 🤖 Testando a IA

### 1. Análise de Sentimento Positivo
```bash
curl -X POST "http://localhost:8000/sentiment/" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Eu amo programar! Python é incrível!"
  }'
```

**Resultado:**
```json
{
  "text": "Eu amo programar! Python é incrível!",
  "label": "POSITIVE",
  "score": 0.9998,
  "interpretation": {
    "sentiment": "Positivo",
    "confidence": "99.8%"
  }
}
```

### 2. Análise de Sentimento Negativo
```bash
curl -X POST "http://localhost:8000/sentiment/" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Odeio quando o código não funciona!"
  }'
```

### 3. Verificar se a IA está funcionando
```bash
curl -X GET "http://localhost:8000/sentiment/health"
```

## 📁 Estrutura do Projeto

```
sentiment-analysis-fastapi/
├── app/                          # Código da API
│   ├── main.py                  # Aplicação principal
│   ├── routers/
│   │   └── sentiment.py         # Lógica da IA
│   ├── models.py                # Schemas de dados
│   └── tests/
│       └── test_api.py          # Testes da IA
├── requirements.txt             # Dependências (incluindo IA)
├── EXEMPLOS.md                  # Exemplos práticos
└── README.md                    # Documentação completa
```

## 🧠 Como a IA Funciona

1. **Modelo**: Usa HuggingFace Transformers (modelo pré-treinado)
2. **Entrada**: Texto em linguagem natural
3. **Processamento**: IA analisa o texto usando redes neurais
4. **Saída**: Label (POSITIVE/NEGATIVE) + score de confiança

## ⚠️ Primeira Execução

Na primeira vez que rodar, a API vai:
1. Baixar o modelo de IA da internet (pode demorar)
2. Carregar o modelo na memória
3. Ficar pronta para análises

**Seja paciente!** Modelos de IA são grandes (centenas de MB).

## 🐛 Problemas Comuns

### Erro 503 - Modelo não disponível
- **Causa**: Modelo ainda está carregando ou falhou
- **Solução**: Aguarde alguns minutos ou reinicie a API

### Erro 422 - Texto inválido
- **Causa**: Texto muito longo (>5000 chars) ou vazio
- **Solução**: Use textos menores e válidos

### Timeout ou lentidão
- **Causa**: Modelo de IA é pesado
- **Solução**: Normal na primeira execução, depois fica rápido

## 🧪 Rodando os Testes

```bash
# Testar tudo
pytest

# Ver detalhes
pytest -v

# Testar só a IA
pytest app/tests/test_api.py -v
```

## 🎯 Casos de Uso

- **Análise de feedback**: Classificar comentários de clientes
- **Monitoramento de redes sociais**: Detectar sentimentos em posts
- **Análise de reviews**: Avaliar opiniões sobre produtos
- **Chatbots**: Entender emoções dos usuários

## 💡 Dicas

1. **Use a documentação**: `/docs` é interativa e fácil de testar
2. **Textos em inglês**: Modelo funciona melhor com inglês
3. **Textos curtos**: Melhor performance com textos menores
4. **Cache**: Resultados similares são mais rápidos

## 🚀 Próximos Passos

1. Teste diferentes tipos de texto
2. Experimente com outros idiomas
3. Analise grandes volumes de dados
4. Integre com suas próprias aplicações

## 📚 Recursos para Aprender Mais

- **HuggingFace**: https://huggingface.co/
- **Transformers**: https://huggingface.co/docs/transformers/
- **FastAPI**: https://fastapi.tiangolo.com/
- **Machine Learning**: https://scikit-learn.org/

---

**Criado por Pedro Vergueiro** - Projeto de aprendizado sobre IA e NLP 🤖