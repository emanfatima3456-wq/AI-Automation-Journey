# Code 1 — System Prompt + User Prompt
import cohere

client = cohere.ClientV2(api_key="your-cohere-key-here")

# System prompt = giving AI a role
# User prompt = your question

response = client.chat(
    model="command-r-08-2024",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant who explains everything in simple English. Always be friendly and clear."
        },
        {
            "role": "user",
            "content": "What is Machine Learning? Explain in 3 simple points."
        }
    ]
)

print(response.message.content[0].text)
# Code 2 — Strict Teacher Prompt
import cohere

client = cohere.ClientV2(api_key="your-cohere-key-here")

response = client.chat(
    model="command-r-08-2024",
    messages=[
        {
            "role": "system",
            "content": "You are a strict teacher who answers in bullet points only. Always use simple words."
        },
        {
            "role": "user",
            "content": "What is Deep Learning?"
        }
    ]
)

print(response.message.content[0].text)
# Code 3 — Creative Poet Prompt
import cohere

client = cohere.ClientV2(api_key="your-cohere-key-here")

response = client.chat(
    model="command-r-08-2024",
    messages=[
        {
            "role": "system",
            "content": "You are a creative poet."
        },
        {
            "role": "user",
            "content": "Write a 4 line poem about AI automation."
        }
    ]
)

print(response.message.content[0].text)
# Code 4 — Structured Output (Most Important!) ⭐
import cohere
import json

client = cohere.ClientV2(api_key="your-cohere-key-here")

response = client.chat(
    model="command-r-08-2024",
    messages=[
        {
            "role": "system",
            "content": "You are an email analyzer. Always respond in JSON format only. No extra text."
        },
        {
            "role": "user",
            "content": """Analyze this email and return JSON:
            Email: 'I ordered my product 10 days ago but haven't received it yet. I am very angry!'
            
            Return this exact JSON:
            {
                "category": "complaint or question or feedback",
                "sentiment": "positive or negative or neutral",
                "priority": "high or medium or low"
            }"""
        }
    ]
)

# Get response text
text = response.message.content[0].text
print("Raw response:", text)

# Convert to JSON
data = json.loads(text)
print("\nCategory:", data["category"])
print("Sentiment:", data["sentiment"])
print("Priority:", data["priority"])
# What We Learned Today:
# Code	Concept	Result
# Code 1	System + User Prompt	Friendly explanation
# Code 2	Strict role	            Bullet points only
# Code 3	Creative role	           AI wrote a poem
# Code 4	Structured Output	       JSON response