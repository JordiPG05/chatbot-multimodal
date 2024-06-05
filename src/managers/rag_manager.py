#Langchain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

# Cargar modulos creados
from src.config.system_rag_prompt import SYSTEM_TEMPLATE

class RAGManager:
    def __init__(self):
        pass
    
    def response_stream(self, docs, prompt, client):
        question_answering_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    SYSTEM_TEMPLATE,
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )
        document_chain = create_stuff_documents_chain(client, question_answering_prompt)
        response = document_chain.stream(
                {
                    "context": docs,
                    "messages": [HumanMessage(content=prompt)]
                }
            )

        return response