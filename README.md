# 🚀 Trade Opportunities API

This FastAPI-based API provides **AI-powered market opportunity analysis reports** for various sectors in the Indian economy. It uses real-time data sources and integrates LLMs like Gemini/OpenAI to generate comprehensive markdown reports.

---

## 📦 Features

- ✅ FastAPI backend with JWT-based authentication
- 🔐 Secure login with token-based access
- 🤖 AI-generated market analysis (Gemini/OpenAI/HuggingFace fallback)
- 🌐 Real-time data fetched from News APIs or scraping
- 📝 Markdown reports saved automatically as `.md` files on the server
- 🧃 Clean RESTful endpoint (`/analyze/{sector}`)
- ⚙️ Rate-limiting to avoid abuse
- 🧪 Interactive Swagger UI for API testing

---

## 🛠️ Setup Instructions

### 🔁 Clone & Navigate

```bash
git clone https://github.com/Dineshbalaji25/Trade-Opportunities.git
cd trade-opportunities-api


## 📥 Install Dependencies

> Use Python 3.10+ recommended

```bash
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows

pip install -r requirements.txt


## ▶️ Run the App

```bash
uvicorn app.main:app --reload

## Swagger UI will be available at:

http://127.0.0.1:8000/docs

## 🔐 Authentication
🔑 Get JWT Token

| Field    | Value      |
| -------- | ---------- |
| username | `admin`    |
| password | `admin123` |


## Example curl:

curl -X POST http://127.0.0.1:8000/token -d "username=admin&password=admin123"

### Response:

{
  "access_token": "your-token-here",
  "token_type": "bearer"
}

## 📊 Analyze Sector

### Endpoint

GET /analyze/{sector}
Authorization: Bearer <your_jwt_token>


Replace `{sector}` with a valid industry (e.g., `e-commerce`, `pharmaceuticals`, `banking`, etc.)

### Example curl

```bash
curl -X GET http://127.0.0.1:8000/analyze/pharmaceuticals \
  -H "Authorization: Bearer <your-token-here>"


📁 Markdown Report Output
Each analysis automatically generates a .md file saved under the reports/ folder.
