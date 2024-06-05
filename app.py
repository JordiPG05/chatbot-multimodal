import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

from src.managers.pdf_extarctor import extract_pdf

# Título de la aplicación
st.title("💬 Chatbot")

# Inicialización del cliente de ChatOllama
client = ChatOllama(model="llama3")

# Inicialización de variables en el estado de sesión
if "ollama" not in st.session_state:
    st.session_state["ollama"] = "llama3"

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]


for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])



# Entrada de texto del usuario
if prompt := st.chat_input():
    # Agregar mensaje del usuario al estado de sesión
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    with st.chat_message("assistant"):
        docs = extract_pdf(query=prompt)
        
        for doc in docs:
            assistant_info = docs[0].page_content
        assistant_promt = f"Never response with you ouw knowledge. Reponse only with de context data: {assistant_info}"
        # Preparar y enviar el mensaje al modelo
        messages = [SystemMessage(content=assistant_promt),
                    HumanMessage(content=prompt)]
        response = client.stream(messages)
        
        # Agregar respuesta del asistente al estado de sesión y mostrarla
        assistant_response = st.write_stream(response)
    st.session_state["messages"].append({"role": "assistant", "content": assistant_response})
    