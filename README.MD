```markdown
# Processo Seletivo - Repositório de Testes

Repositório contendo 4 desafios técnicos desenvolvidos em Python e Vue.js.

## 📋 Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)
- Node.js 16+ (apenas para Teste 4)
- Ghostscript (obrigatório para Teste 2)

## 🛠 Configuração do Ambiente

### Ambiente Virtual (Windows)
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Ambiente Virtual (MacOS/Linux)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🧪 Teste 1 - Web Scraping
**Arquivo:** `tiny_scraper.py`

**Instruções:**
```bash
python tiny_scraper.py
```
**Saída:**
- Dados brutos em `Teste-01/src/data`
- Arquivo compactado em `Teste-01/src/compressed`

---

## 🧪 Teste 2 - Extração de PDF com Camelot
**Arquivo:** `camelot_ride.py`

### Instalar Ghostscript
**Windows:**
1. Baixe o instalador em [https://www.ghostscript.com](https://www.ghostscript.com)
2. Adicione ao PATH durante a instalação

**MacOS:**
```bash
brew install ghostscript
```

**Linux (Debian/Ubuntu):**
```bash
sudo apt-get install ghostscript
```

**Execução:**
```bash
python camelot_ride.py
```
**Saída:** Arquivos CSV em `Teste-02/csv`

---

## 🧪 Teste 3 - Modelagem de Banco de Dados
**Pré-requisito:** 
1. Extrair arquivos ZIP CSV-2023 e CSV-2024 para as respectivas pastas:
   - `Teste-03/Data/2023`
   - `Teste-03/Data/2024`

**Etapas:**
1. Sanitizar dados:
```bash
python csv_sanitizer.py
```
2. Executar scripts .sql:
```bash
# URI para consulta do banco tembo: postgresql://readonly:7iaAxSNMcUjhJC2l@suavely-developed-whitebait.data-1.use1.tembo.io:5432/postgres
psql -<URI> -f CriarTabelas.sql
psql -<URI> -f query-ultimo-ano.sql
psql -<URI> -f query-ultimo-trimestre.sql
```
---

## 🧪 Teste 4 - Frontend/Backend Integrado

### Backend (Flask)
**Diretório:** `/back-end`
```bash
python start_app.py
```
**Endpoint:** `http://localhost:8080/operadoras/search?page=[PARAMETRO]`

Busca válidas por:
- `cnpj`
- `registro`
- `razao_social`
- `nome_fantasia`

Corpo da requisição:

```json
{
  "search": "CNPJ", // ou Registro_ANS ou Nome_Fantasia ou Razao_Social,
  "value": "146" // ou valor de texto
}
```

### Frontend (Vue.js)
**Diretório:** `/front-end/teste-04-front`
```bash
npm install
npm run dev
```
**Acesso:** `http://localhost:5173`

---

## 📦 Dependências
Todas as dependências Python estão em `requirements.txt`. 

Para frontend:
- Vue 3
- Axios
- Vue Router

## ⚠️ Notas Importantes
- Mantenha as pastas de dados conforme estrutura original
- O Teste 3 requer conexão ativa com o PostgreSQL
- Portas padrão: 8080 (backend) e 5173 (frontend)
```
