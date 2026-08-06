# 🤖 AI Business Automation Suite

> An end-to-end AI-powered lead management system that automatically scores leads, generates personalized emails, and sends them — with zero manual work!

---

## ✨ Features

- 🎯 **Smart Lead Scoring** — ML model scores leads as Hot/Warm/Cold instantly
- 🤖 **AI Email Generation** — Cohere AI writes personalized emails automatically
- 📨 **Auto Email Delivery** — Make.com sends emails to clients automatically
- 📊 **Live Dashboard** — Real-time charts, stats, and lead history
- 💰 **Budget Slider** — Interactive budget selection with category labels
- 🌙 **Dark Professional UI** — Beautiful React interface

---

## 🏗️ System Architecture

```
React Frontend (Lead Form + Dashboard)
        ↓
FastAPI Backend (Python)
        ↓
ML Model — Scikit-learn (Hot/Warm/Cold Scoring)
        ↓
Cohere AI (Personalized Email Generation)
        ↓
Make.com Automation (Auto Email Send)
        ↓
Gmail (Email Delivered to Client) ✅
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | React + Vite + Tailwind CSS |
| **Backend** | FastAPI (Python) |
| **ML Model** | Scikit-learn |
| **AI** | Cohere API (command-r-08-2024) |
| **Automation** | Make.com |
| **Charts** | Recharts |
| **HTTP Client** | Axios |

---

## 📁 Project Structure

```
AI-Business-Suite/
├── main.py                 # FastAPI backend
├── .env                    # API keys (not in repo)
├── requirements.txt        # Python dependencies
└── frontend/
    ├── src/
    │   ├── App.jsx
    │   ├── pages/
    │   │   ├── LeadForm.jsx    # Lead submission form
    │   │   └── Dashboard.jsx   # Analytics dashboard
    │   └── components/
    │       └── Navbar.jsx
    └── package.json
```

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/emanfatima3456-wq/AI-Automation-Journey.git
cd 09-Projects/AI-Business-Suite
```

### 2. Backend Setup
```bash
pip install fastapi uvicorn scikit-learn cohere python-dotenv
```

Create `.env` file:
```
COHERE_API_KEY=your_cohere_api_key
```

Run FastAPI:
```bash
uvicorn main:app --reload
```

### 3. Frontend Setup
```bash
cd frontend
npm install --legacy-peer-deps
npm run dev
```

### 4. Open Browser
```
Frontend:  http://localhost:5174
API Docs:  http://localhost:8000/docs
```

---

## 📊 How It Works

### Step 1 — Fill Lead Form
Client fills: Name, Email, Company, Budget (slider), Requirements

### Step 2 — ML Scoring
```python
if budget >= 50000:     → 🔥 Hot Lead
elif budget >= 20000:   → ⚡ Warm Lead  
else:                   → ❄️ Cold Lead
```

### Step 3 — AI Email
Cohere AI generates personalized email based on lead score

### Step 4 — Auto Send
Make.com webhook automatically sends email to client via Gmail

### Step 5 — Dashboard
Real-time stats, pie chart, and lead history table updated instantly

---

## 🔑 Environment Variables

```
COHERE_API_KEY=your_key_here
```

---

## 📸 Screenshots

| Lead Form | Dashboard |
|---|---|
| <img width="608" height="421" alt="image" src="https://github.com/user-attachments/assets/a5bb2823-8545-4bb3-8260-da604907822a" />
  <img width="563" height="413" alt="image" src="https://github.com/user-attachments/assets/6d21d5ad-57cc-4039-b916-5a7ef05ee3b3" />
 
 |<img width="914" height="350" alt="image" src="https://github.com/user-attachments/assets/7158a1c7-eaaf-4a8f-9834-8387b2d815a0" />
  |<img width="739" height="258" alt="image" src="https://github.com/user-attachments/assets/7a1ef791-dd7c-4cf5-a14d-b5ebc7d903f9" />



---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| POST | `/analyze-lead` | Analyze lead + generate email |

### Sample Request:
```json
{
  "name": "Ahmed Khan",
  "email": "ahmed@techcorp.com",
  "company": "TechCorp",
  "budget": 75000,
  "requirements": "Need an AI system urgently"
}
```

### Sample Response:
```json
{
  "name": "Ahmed Khan",
  "lead_score": "Hot",
  "ai_email": "Dear Ahmed Khan, I am thrilled...",
  "status": "success"
}
```

---

## 🎯 Part of AI Automation Journey

| Project | Tech | Status |
|---|---|---|
| P1 — AI Email Assistant | Python + Cohere + Streamlit | ✅ Live |
| P2 — AI Lead Management | n8n + Cohere + Sheets | ✅ Complete |
| **P3 — AI Business Suite** | **React + FastAPI + ML + Make.com** | **✅ Complete** |
| P4 — Chat with PDF | LangChain + ChromaDB | ⏳ Next |
| P5 — AI Research Agent | CrewAI + LangGraph | ⏳ Coming |
| P6 — Live AI API | FastAPI + Docker | ⏳ Coming |

---

## 👩‍💻 Author

**Eman Fatima**
- GitHub: [@emanfatima3456-wq](https://github.com/emanfatima3456-wq)
- LinkedIn: [https://www.linkedin.com/in/eman-fatima-251062402/]

---

## ⭐ If you found this helpful, please star the repo!
