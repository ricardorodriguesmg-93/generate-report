import os
import sys
from google import genai
from google.genai import types

from config import MODEL_NAME, SYSTEM_INSTRUCTION_2

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERRO: A variável de ambiente GEMINI_API_KEY não foi definida.")
        print("Defina a variável com: export GEMINI_API_KEY='sua_chave'")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    print("=== Agente de Relatórios Pedagógicos - Baby Nap ===")
    print("Insira/cole as observações do aluno (prima Ctrl+D ou Ctrl+Z no Windows para finalizar):\n")

    input_texto = sys.stdin.read()

    if not input_texto.strip():
        print("Nenhum texto fornecido. A encerrar.")
        return

    print("\n[+] A gerar relatório com o Gemini...\n")
    
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=input_texto,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION_2,
            temperature=0.3,
            response_mime_type="application/json"
        )
    )

    relatorio = response.text
    print(relatorio)

    nome_ficheiro = "relatorio_saida.txt"
    with open(nome_ficheiro, "w", encoding="utf-8") as f:
        f.write(relatorio)

    print(f"\n[✓] Relatório guardado no ficheiro '{nome_ficheiro}'.")

if __name__ == "__main__":
    main()
