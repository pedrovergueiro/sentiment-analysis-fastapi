#!/usr/bin/env python3
"""
🚀 Script para rodar a Sentiment Analysis API

Execute este arquivo para iniciar o servidor de desenvolvimento.
Comando: python run.py

Autor: Pedro Vergueiro
Projeto: API de Análise de Sentimentos com IA
"""

import uvicorn
import os
import sys

def check_dependencies():
    """Verifica se as dependências estão instaladas"""
    try:
        import fastapi
        import transformers
        import torch
        print("✅ Dependências principais encontradas")
        return True
    except ImportError as e:
        print(f"❌ Dependência faltando: {e}")
        print("💡 Execute: pip install -r requirements.txt")
        return False

def main():
    """Função principal para iniciar a API"""
    print("🤖 Iniciando Sentiment Analysis API...")
    print("📚 Documentação: http://localhost:8000/docs")
    print("🏥 Status da IA: http://localhost:8000/sentiment/health")
    print("🔄 Pressione Ctrl+C para parar")
    print()
    
    # Verificar dependências
    if not check_dependencies():
        sys.exit(1)
    
    # Avisos importantes
    print("⚠️  PRIMEIRA EXECUÇÃO:")
    print("   - Modelo de IA será baixado (pode demorar)")
    print("   - Aguarde 'Modelo de IA carregado com sucesso!'")
    print("   - Depois disso, a API estará pronta!")
    print()
    
    try:
        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,  # Reinicia automaticamente quando o código muda
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n🛑 API interrompida pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro ao iniciar API: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()