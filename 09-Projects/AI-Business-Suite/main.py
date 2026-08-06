from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import cohere
import uvicorn
from pyngrok import ngrok
from dotenv import load_dotenv
import os

load_dotenv()

co = os.getenv("COHERE_API_KEY")
# --- Auth ---
ngrok.set_auth_token("3HVCGRG2MizUn5RLI5Is2AoJVRS_2kaGY9219WE1HFEnUtLgY")


# --- App ---
app = FastAPI(title="AI Business Suite")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Schema ---
class Lead(BaseModel):
    name: str
    email: str
    company: str
    budget: float
    requirements: str

# --- ML Model ---
X_train = np.array([
    [100000, 50, 1],
    [75000,  30, 0],
    [60000,  40, 1],
    [50000,  20, 0],
    [30000,  25, 1],
    [25000,  15, 0],
    [20000,  10, 0],
    [10000,  8,  0],
    [5000,   5,  0],
    [3000,   4,  0],
])
y_train = np.array([2, 2, 2, 2, 1, 1, 1, 0, 0, 0])

ml_model = RandomForestClassifier(n_estimators=100, random_state=42)
ml_model.fit(X_train, y_train)

label_map = {0: "Cold", 1: "Warm", 2: "Hot"}

# --- Helpers ---
def extract_features(budget: float, requirements: str):
    urgent_words = ["urgent", "asap", "immediately", "quickly", "soon"]
    has_urgent = int(any(w in requirements.lower() for w in urgent_words))
    return np.array([[budget, len(requirements), has_urgent]])


def generate_email(lead_score: str, name: str, company: str, budget: float, requirements: str) -> str:
    prompt = f"""Write a short professional email to this lead:

Name: {name}
Company: {company}
Budget: ${budget}
Requirements: {requirements}
Lead Score: {lead_score}

Write a personalized 3-4 line email based on their score:
- Hot: Urgent, excited tone
- Warm: Friendly, informative tone
- Cold: Simple, brief tone

Email:"""
    response = co.chat(model="command-r-08-2024", message=prompt)
    return response.text

# --- Routes ---
@app.get("/")
def home():
    return {"message": "Welcome to AI Business Suite!"}


@app.post("/analyze-lead")
def analyze_lead(lead: Lead):
    features = extract_features(lead.budget, lead.requirements)
    prediction = ml_model.predict(features)[0]
    confidence = ml_model.predict_proba(features)[0].max()
    lead_score = label_map[prediction]
    email_content = generate_email(lead_score, lead.name, lead.company, lead.budget, lead.requirements)

    return {
        "name": lead.name,
        "email": lead.email,
        "company": lead.company,
        "budget": lead.budget,
        "requirements": lead.requirements,
        "lead_score": lead_score,
        "confidence": round(float(confidence) * 100, 2),
        "ai_email": email_content,
        "status": "success"
    }

# --- Entry Point ---
if __name__ == "__main__":
    public_url = ngrok.connect(8000)
    print(f"Public URL: {public_url}")
    print(f"Endpoint:   {public_url}/analyze-lead")
    uvicorn.run(app, host="0.0.0.0", port=8000)