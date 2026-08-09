from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    model="openrouter/auto"
)
Chat_history = []
def chat(user_message):
    Chat_history.append(HumanMessage(content=user_message))
    response = llm.invoke(Chat_history)
    Chat_history.append(AIMessage(content=response.content))
    return response.content
print("User: My name is Eman and I live in Pakistan")
response1 = chat("My name is Eman and I live in Pakistan")
print(f"AI: {response1}")
print("---")

print("User: I am learning AI automation")
response2 = chat("I am learning AI automation")
print(f"AI: {response2}")
print("---")

print("User: What is my name and what am I learning?")
response3 = chat("What is my name and what am I learning?")
print(f"AI: {response3}")
         
         
         
         
         
        