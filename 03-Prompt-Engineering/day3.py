# import cohere
# client = cohere.ClientV2(api_key="b1uAEIebpoSaJqifrFkp2kpMjoxlBXP2nDoKwZ9b")
# response = client.chat(
#     model="command-r-08-2024",
#     messages=[
#    {
#             "role": "system",
#             "content": "You are a creative poet."
#         },
#         {
#             "role": "user",
#             "content": "Write a 4 line poem about AI automation."
#         }
#     ]
# )
# print(response.message.content[0].text)
import cohere
import json

client = cohere.ClientV2(api_key="b1uAEIebpoSaJqifrFkp2kpMjoxlBXP2nDoKwZ9b")

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