import chromadb

# ChromaDB client banao
client = chromadb.Client()

# Collection banao — jaise database table
collection = client.create_collection("my_documents")

# Documents add karo
collection.add(
    documents=[
        "Eman is learning AI automation in Pakistan",
        "Project 3 was built with React and FastAPI",
        "LangChain is a framework for AI applications",
        "ChromaDB is a vector database for AI"
    ],
    ids=["doc1", "doc2", "doc3", "doc4"]
)

# Query karo — similar documents dhundho
results = collection.query(
    query_texts=["What is Eman learning?"],
    n_results=2
)

print("Query: What is Eman learning?")
print("Results:")
for doc in results['documents'][0]:
    print(f"→ {doc}")