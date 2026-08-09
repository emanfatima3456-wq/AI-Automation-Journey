from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Document load karo
loader = TextLoader("sample.txt")
documents = loader.load()

print(f"Document loaded!")
print(f"Total characters: {len(documents[0].page_content)}")
print(f"Content preview: {documents[0].page_content[:200]}")
print("---")

# Text splitter — document ko chunks mein todo
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

chunks = splitter.split_documents(documents)

print(f"Total chunks: {len(chunks)}")
print("---")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk.page_content}")
    print("---")