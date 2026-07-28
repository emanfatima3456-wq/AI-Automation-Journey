# 🤖 AI Email Assistant

> An AI-powered email analyzer that automatically detects category, 
> sentiment, priority and generates professional replies instantly!

🔗 **Live Demo:** [Try it here!](https://ai-email-assistant-eman.streamlit.app/)

---

## 📌 What Problem Does It Solve?

Companies receive hundreds of emails daily. Manually reading, 
categorizing and replying to each email wastes hours of time.

This tool automates the entire process in seconds using AI!

---

## ⚡ Features

| Feature | Description |
|---------|-------------|
| 📧 Category Detection | Complaint, Question or Feedback |
| 💬 Sentiment Analysis | Positive, Negative or Neutral |
| 🚨 Priority Setting | High, Medium or Low |
| ✍️ Auto Reply | Professional reply generated instantly |
| 🎨 Clean UI | Built with Streamlit |

---

## 🛠️ Tech Stack

- **Python** — Core programming language
- **Cohere AI API** — Large Language Model
- **Prompt Engineering** — Structured AI responses
- **Streamlit** — Web UI framework

---

## 📂 Project Structure
AI-Email-Assistant/
├── app.py # Streamlit UI
├── email_assistant.py # AI logic
├── requirements.txt # Dependencies
└── README.md # Documentation
---

## ⚙️ How To Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/emanfatima3456-wq/AI-Automation-Journey.git
cd 09-Projects/AI-Email-Assistant
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your API key in `email_assistant.py`**
```python
client = cohere.ClientV2(api_key="your-key-here")
```

**4. Run the app**
```bash
streamlit run app.py
```

---

## 📊 Example Output

**Input Email:**
> "I ordered my product 15 days ago but haven't received it. 
> I am extremely frustrated!"

**AI Output:**
Category: COMPLAINT
Sentiment: NEGATIVE
Priority: HIGH

Suggested Reply:
Dear Customer, we sincerely apologize for the delay...
---

## 🖼️ Screenshot

![AI Email Assistant](screenshot.png)

---

## 👩‍💻 Developer

**Eman Fatima**
- 🔗 GitHub: [@emanfatima3456-wq](https://github.com/emanfatima3456-wq)
- 💼 LinkedIn: [Your LinkedIn URL]

---

## 🌟 Part of AI Automation Journey

This is **Project 1** of my AI Automation portfolio.
More projects coming soon!

---

⭐ If you like this project, please give it a star!
