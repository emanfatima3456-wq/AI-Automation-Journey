import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from gtts import gTTS
import chromadb
import tempfile
import os
from dotenv import load_dotenv

load_dotenv()

# Page config
st.set_page_config(
    page_title="Chat with PDF",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Chat with PDF + Voice 🎤")
st.markdown("Upload any PDF and ask questions!")

# AI Setup
llm = ChatOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    model="openrouter/auto"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful assistant. 
    Answer questions based on this context: {context}
    If answer is not in context, say 'This information is not in the document.'"""),
    ("human", "{question}")
])

chain = prompt | llm | StrOutputParser()

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "collection" not in st.session_state:
    st.session_state.collection = None

# Sidebar - PDF Upload
with st.sidebar:
    st.header("📁 Upload PDF")
    uploaded_file = st.file_uploader("Choose PDF", type="pdf")
    if uploaded_file:
        if st.button("🔄 Process PDF"):
            with st.spinner("Processing PDF..."):
                # Temp file banao
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(uploaded_file.read())
                    tmp_path = tmp.name
                
                # PDF load karo
                loader = PyPDFLoader(tmp_path)
                documents = loader.load()
                
                # Chunks banao
                splitter = RecursiveCharacterTextSplitter(
                    chunk_size=500,
                    chunk_overlap=50
                )
                chunks = splitter.split_documents(documents)
                
                # ChromaDB mein store karo
                client = chromadb.Client()
                try:
                    client.delete_collection("pdf_docs")
                except:
                    pass
                
                collection = client.create_collection("pdf_docs")
                collection.add(
                    documents=[chunk.page_content for chunk in chunks],
                    ids=[f"chunk_{i}" for i in range(len(chunks))]
                )
                
                st.session_state.collection = collection
                st.session_state.messages = []
                os.unlink(tmp_path)
                
            st.success(f"✅ PDF processed! {len(chunks)} chunks created!")
            st.info(f"📄 Pages: {len(documents)}")

# Main Chat Area
if st.session_state.collection:
    st.header("💬 Ask Questions")
    
    # Chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    
    # Input
    question = st.chat_input("Ask anything about your PDF...")
    
    if question:
        # User message
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })
        with st.chat_message("user"):
            st.write(question)
        
        # AI answer
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # ChromaDB se context lo
                results = st.session_state.collection.query(
                    query_texts=[question],
                    n_results=3
                )
                context = " ".join(results['documents'][0])
                
                # AI se jawab lo
                answer = chain.invoke({
                    "context": context,
                    "question": question
                })
                
                st.write(answer)
                
                # Voice output
                tts = gTTS(text=answer, lang='en')
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                    tts.save(fp.name)
                    st.audio(fp.name, format="audio/mp3")
                
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

else:
    st.info("👈 Please upload a PDF from the sidebar to start!")
    st.markdown("""
    ### How to use:
    1. 📁 Upload any PDF from sidebar
    2. 🔄 Click 'Process PDF'
    3. 💬 Ask questions!
    4. 🔊 Listen to voice answers!
    """)