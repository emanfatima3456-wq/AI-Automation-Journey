import cohere
import json

client = cohere.ClientV2(api_key="b1uAEIebpoSaJqifrFkp2kpMjoxlBXP2nDoKwZ9b")

def analyze_email(email_text):
    response = client.chat(
        model="command-r-08-2024",
        messages=[
            {
                "role": "system",
                "content": "You are an expert email analyzer. Always respond in JSON format only. No extra text."
            },
            {
                "role": "user",
                "content": f"""Analyze this email and return JSON:
                Email: '{email_text}'
                
                Return this exact JSON:
                {{
                    "category": "complaint or question or feedback",
                    "sentiment": "positive or negative or neutral",
                    "priority": "high or medium or low",
                    "reply": "write a professional reply here"
                }}"""
            }
        ]
    )
    
    text = response.message.content[0].text
    data = json.loads(text)
    return data