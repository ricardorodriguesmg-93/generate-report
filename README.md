# Agente de Relatórios Pedagógicos - Baby Nap

Aplicação local para geração de relatórios pedagógicos infantis utilizando a API Google Gemini 2.5 Flash.

## 🚀 Como Instalar e Executar

### 1. Requisitos Prévios
- Python 3.9 ou superior instalado.
- Chave de API gratuita do Google AI Studio (https://aistudio.google.com/).

### 2. Instalar as Dependências
No terminal, dentro da pasta do projeto, execute:
```bash
pip install -r requirements.txt
```

### 3. Configurar a Chave de API
Configure a sua chave de API no terminal:

- **Linux / macOS:**
  ```bash
  export GEMINI_API_KEY="SUA_CHAVE_AQUI"
  ```
- **Windows (CMD):**
  ```cmd
  set GEMINI_API_KEY="SUA_CHAVE_AQUI"
  ```
- **Windows (PowerShell):**
  ```powershell
  $env:GEMINI_API_KEY="SUA_CHAVE_AQUI"
  ```

---

## 🛠️ Como Executar

### Opção A: Interface Web no Navegador (Recomendado)
Execute o comando:
```bash
streamlit run app.py
```
O navegador abrirá automaticamente no endereço `http://localhost:8501`, onde poderá colar o rascunho do aluno e descarregar o relatório em Word (`.docx`).

### Opção B: Execução via Terminal
Execute o comando:
```bash
python cli.py
```
Cole o rascunho do aluno no terminal e prima `Ctrl+D` (Linux/Mac) ou `Ctrl+Z` (Windows) seguido de Enter.
