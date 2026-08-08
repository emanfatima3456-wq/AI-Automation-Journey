from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    model="openrouter/auto"
)


# Step 1 — Lead Score karo
score_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a lead scoring expert. Reply with ONLY one word: Hot, Warm, or Cold"),
    ("human", "Budget: ${budget}, Requirements: {requirements}")
])

# Step 2 — Email likho
email_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a professional email writer."),
    ("human", "Write a short follow-up email for a {score} lead named {name}")
])

parser = StrOutputParser()

# Chain 1 — Scoring
score_chain = score_prompt | llm | parser

# Chain 2 — Email
email_chain = email_prompt | llm | parser

# Run karo
score = score_chain.invoke({
    "budget": "75000",
    "requirements": "Need AI system urgently"
})

print(f"Lead Score: {score}")

email = email_chain.invoke({
    "score": score,
    "name": "Sara Ahmed"
})

print(f"\nAI Email:\n{email}")