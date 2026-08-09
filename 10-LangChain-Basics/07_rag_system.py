from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import chromadb
from dotenv import load_dotenv
import os

load_dotenv()

# Step 1: Document Load karo
print("Loading document...")
loader = TextLoader("sample.txt")
documents = loader.load()

# Step 2: Chunks banao
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)
chunks = splitter.split_documents(documents)
print(f"Created {len(chunks)} chunks!")

# Step 3: ChromaDB mein store karo
print("Storing in ChromaDB...")
client = chromadb.Client()
collection = client.create_collection("company_docs")

collection.add(
    documents=[chunk.page_content for chunk in chunks],
    ids=[f"chunk_{i}" for i in range(len(chunks))]
)
print("Stored successfully!")

# Step 4: AI Setup
llm = ChatOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    model="openrouter/auto"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer the question based on this context: {context}"),
    ("human", "{question}")
])

chain = prompt | llm | StrOutputParser()

# Step 5: Question puchho!
def ask(question):
    # ChromaDB se relevant chunks dhundho
    results = collection.query(
        query_texts=[question],
        n_results=2
    )
    context = " ".join(results['documents'][0])
    
    # AI se jawab lo
    answer = chain.invoke({
        "context": context,
        "question": question
    })
    return answer

# Test karo!
print("\n" + "="*50)
print("RAG System Ready! Asking questions...")
print("="*50)

q1 = "What is the pricing of Basic Plan?"
print(f"\nQ: {q1}")
print(f"A: {ask(q1)}")

q2 = "What services does TechCorp offer?"
print(f"\nQ: {q2}")
print(f"A: {ask(q2)}")

q3 = "How can I contact TechCorp?"
print(f"\nQ: {q3}")
print(f"A: {ask(q3)}")