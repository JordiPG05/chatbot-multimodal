# Streamlit
import streamlit as st

#Langchain
from langchain_community.chat_models import ChatOllama

# Cargar modulos creados
from src.managers.pdf_extarctor import PDFExtractor
from src.managers.rag_manager import RAGManager

rag_manager = RAGManager()
pdf_extractor = PDFExtractor()

# Título de la aplicación
st.title("💬 Chatbot")

# Inicialización del cliente de ChatOllama
client = ChatOllama(model="llama3")

# Inicialización de variables en el estado de sesión
if "ollama" not in st.session_state:
    st.session_state["ollama"] = "llama3"

# Crear el hisorial de mensajes
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Guardar el mensaje en el historial
for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

# Entrada de texto del usuario
if prompt := st.chat_input():
    # Agregar mensaje del usuario al estado de sesión
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Extraer contenido del PDF
    docs = pdf_extractor.extract_pdf(query=prompt)

    response = rag_manager.response_stream(docs=docs, prompt=prompt, client=client)

    # Agregar respuesta del asistente al estado de sesión y mostrarla
    st.session_state["messages"].append({"role": "assistant", "content": response})
    st.chat_message("assistant").write_stream(response)
