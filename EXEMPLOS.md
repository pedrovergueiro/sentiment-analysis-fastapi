# 📚 Exemplos de Uso da Sentiment Analysis API

Este arquivo contém exemplos práticos de como usar minha API de análise de sentimentos com IA.

## 🚀 Iniciando a API

```bash
# Método 1: Direto com uvicorn
uvicorn app.main:app --reload

# Método 2: Com Docker (se disponível)
docker-compose up
```

## 🌐 Testando no Navegador

Após iniciar a API, abra no navegador:
- **Documentação interativa**: http://localhost:8000/docs
- **Página inicial**: http://localhost:8000/
- **Status do modelo**: http://localhost:8000/sentiment/health

## 🤖 Exemplos com cURL

### 1. Analisar sentimento positivo
```bash
curl -X POST "http://localhost:8000/sentiment/" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Eu amo programar em Python! É incrível!"
  }'
```

**Resposta esperada:**
```json
{
  "text": "Eu amo programar em Python! É incrível!",
  "label": "POSITIVE",
  "score": 0.9998,
  "interpretation": {
    "sentiment": "Positivo",
    "confidence": "99.8%"
  }
}
```

### 2. Analisar sentimento negativo
```bash
curl -X POST "http://localhost:8000/sentiment/" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Odeio bugs no meu código. Isso é terrível!"
  }'
```

### 3. Verificar saúde do modelo
```bash
curl -X GET "http://localhost:8000/sentiment/health"
```

## 🐍 Exemplos com Python

### Usando requests
```python
import requests
import json

# URL base da API
BASE_URL = "http://localhost:8000"

def analisar_sentimento(texto):
    """Analisa o sentimento de um texto"""
    response = requests.post(
        f"{BASE_URL}/sentiment/", 
        json={"text": texto}
    )
    
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 503:
        print("❌ Modelo de IA não está disponível")
        return None
    else:
        print(f"❌ Erro: {response.status_code}")
        return None

# Exemplos de uso
textos_teste = [
    "Adoro trabalhar com FastAPI!",
    "Este bug está me deixando louco...",
    "Python é uma linguagem incrível para IA",
    "Não consigo fazer esse código funcionar",
    "Finalmente consegui resolver o problema! 🎉"
]

print("🤖 Testando análise de sentimentos:")
print("=" * 50)

for texto in textos_teste:
    resultado = analisar_sentimento(texto)
    
    if resultado:
        sentimento = resultado['interpretation']['sentiment']
        confianca = resultado['interpretation']['confidence']
        
        print(f"📝 Texto: {texto}")
        print(f"😊 Sentimento: {sentimento}")
        print(f"🎯 Confiança: {confianca}")
        print("-" * 30)
```

### Usando httpx (async)
```python
import asyncio
import httpx

async def analisar_sentimentos_async(textos):
    """Analisa múltiplos textos de forma assíncrona"""
    async with httpx.AsyncClient() as client:
        tasks = []
        
        for texto in textos:
            task = client.post(
                "http://localhost:8000/sentiment/", 
                json={"text": texto}
            )
            tasks.append(task)
        
        responses = await asyncio.gather(*tasks)
        
        resultados = []
        for response in responses:
            if response.status_code == 200:
                resultados.append(response.json())
            else:
                resultados.append(None)
        
        return resultados

# Exemplo de uso
textos = [
    "FastAPI é incrível!",
    "Odeio quando o código não funciona",
    "Machine Learning é fascinante"
]

# Executar análise assíncrona
resultados = asyncio.run(analisar_sentimentos_async(textos))

for i, resultado in enumerate(resultados):
    if resultado:
        print(f"Texto {i+1}: {resultado['interpretation']['sentiment']}")
```

## 📊 Casos de Uso Práticos

### 1. Análise de Feedback de Clientes
```python
def analisar_feedback_clientes(feedbacks):
    """Analisa sentimentos de uma lista de feedbacks"""
    positivos = 0
    negativos = 0
    
    for feedback in feedbacks:
        resultado = analisar_sentimento(feedback)
        
        if resultado and resultado['label'] == 'POSITIVE':
            positivos += 1
        elif resultado and resultado['label'] == 'NEGATIVE':
            negativos += 1
    
    total = len(feedbacks)
    print(f"📊 Análise de {total} feedbacks:")
    print(f"😊 Positivos: {positivos} ({positivos/total*100:.1f}%)")
    print(f"😞 Negativos: {negativos} ({negativos/total*100:.1f}%)")

# Exemplo
feedbacks_exemplo = [
    "Produto excelente, recomendo!",
    "Entrega demorou muito, decepcionante",
    "Atendimento foi perfeito",
    "Qualidade deixou a desejar"
]

analisar_feedback_clientes(feedbacks_exemplo)
```

### 2. Monitoramento de Comentários
```python
def monitorar_comentarios(comentarios):
    """Monitora comentários e alerta para negativos"""
    for i, comentario in enumerate(comentarios):
        resultado = analisar_sentimento(comentario)
        
        if resultado:
            if resultado['label'] == 'NEGATIVE' and resultado['score'] > 0.8:
                print(f"🚨 ALERTA: Comentário muito negativo detectado!")
                print(f"📝 Comentário {i+1}: {comentario}")
                print(f"🎯 Confiança: {resultado['interpretation']['confidence']}")
                print("-" * 40)

# Exemplo
comentarios = [
    "Adorei o produto!",
    "Péssimo atendimento, nunca mais compro aqui!",
    "Produto ok, nada demais",
    "Horrível! Perda de tempo e dinheiro!"
]

monitorar_comentarios(comentarios)
```

### 3. Análise de Reviews de Produtos
```python
def analisar_reviews_produto(reviews):
    """Analisa reviews e gera relatório"""
    scores_positivos = []
    scores_negativos = []
    
    for review in reviews:
        resultado = analisar_sentimento(review)
        
        if resultado:
            if resultado['label'] == 'POSITIVE':
                scores_positivos.append(resultado['score'])
            else:
                scores_negativos.append(resultado['score'])
    
    if scores_positivos:
        media_positivos = sum(scores_positivos) / len(scores_positivos)
        print(f"😊 Reviews Positivos: {len(scores_positivos)}")
        print(f"📈 Confiança Média: {media_positivos:.3f}")
    
    if scores_negativos:
        media_negativos = sum(scores_negativos) / len(scores_negativos)
        print(f"😞 Reviews Negativos: {len(scores_negativos)}")
        print(f"📉 Confiança Média: {media_negativos:.3f}")

# Exemplo
reviews = [
    "Produto incrível, superou expectativas!",
    "Qualidade excelente, recomendo muito",
    "Não gostei, produto veio com defeito",
    "Péssima experiência de compra"
]

analisar_reviews_produto(reviews)
```

## 🧪 Testando a API

### Executar testes automatizados
```bash
# Rodar todos os testes
pytest

# Ver detalhes dos testes
pytest -v

# Testar só a API
pytest app/tests/test_api.py -v

# Testar com cobertura
pytest --cov=app
```

### Teste manual com diferentes idiomas
```python
# Testando com diferentes idiomas
textos_multilinguais = [
    "I love this product!",  # Inglês
    "Eu amo este produto!",  # Português
    "¡Me encanta este producto!",  # Espanhol
    "J'adore ce produit!",  # Francês
]

for texto in textos_multilinguais:
    resultado = analisar_sentimento(texto)
    if resultado:
        print(f"🌍 {texto} → {resultado['interpretation']['sentiment']}")
```

## ❌ Tratamento de Erros

### Exemplo de tratamento robusto
```python
def analisar_com_tratamento_erro(texto):
    """Análise com tratamento completo de erros"""
    try:
        response = requests.post(
            "http://localhost:8000/sentiment/", 
            json={"text": texto},
            timeout=10  # Timeout de 10 segundos
        )
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 503:
            print("⚠️ Modelo temporariamente indisponível")
            return {"error": "model_unavailable"}
        elif response.status_code == 422:
            print("❌ Texto inválido (muito longo ou vazio)")
            return {"error": "invalid_text"}
        else:
            print(f"❌ Erro HTTP: {response.status_code}")
            return {"error": f"http_{response.status_code}"}
            
    except requests.exceptions.Timeout:
        print("⏰ Timeout: API demorou para responder")
        return {"error": "timeout"}
    except requests.exceptions.ConnectionError:
        print("🔌 Erro de conexão: API não está rodando?")
        return {"error": "connection_error"}
    except Exception as e:
        print(f"💥 Erro inesperado: {e}")
        return {"error": "unexpected"}

# Exemplo de uso robusto
resultado = analisar_com_tratamento_erro("Texto de teste")
if resultado and "error" not in resultado:
    print(f"✅ Análise: {resultado['interpretation']['sentiment']}")
else:
    print("❌ Não foi possível analisar o texto")
```

## 🎯 Dicas de Performance

1. **Reutilize conexões**: Use `requests.Session()` para múltiplas requisições
2. **Processamento em lote**: Analise múltiplos textos de forma assíncrona
3. **Cache local**: Armazene resultados para textos repetidos
4. **Timeout adequado**: Configure timeouts para evitar travamentos

## 🔧 Troubleshooting

### Problemas comuns:

1. **Erro 503 (Modelo indisponível)**:
   - Primeira execução: modelo está sendo baixado
   - Sem internet: modelo não consegue ser carregado
   - Solução: aguarde ou verifique conexão

2. **Erro 422 (Validação)**:
   - Texto muito longo (>5000 caracteres)
   - Texto vazio
   - Solução: valide entrada antes de enviar

3. **Timeout**:
   - Modelo pesado pode demorar
   - Solução: aumente timeout ou use versão mais leve

4. **Conexão recusada**:
   - API não está rodando
   - Solução: inicie com `uvicorn app.main:app --reload`