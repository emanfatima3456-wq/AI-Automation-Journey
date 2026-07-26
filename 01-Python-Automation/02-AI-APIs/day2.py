import cohere

# API Key here
client = cohere.ClientV2(api_key="b1uAEIebpoSaJqifrFkp2kpMjoxlBXP2nDoKwZ9b")

# Send message to AI
response = client.chat(
    model="command-r-08-2024",
    messages=[
      {"role": "user", "content": "What is AI Automation? Explain in simple words"}
    ]
)

# Print AI response
print(response.message.content[0].text)