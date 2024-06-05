from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

def extract_pdf(query):
    loader = PyPDFLoader("src/data/DEEP_LEARNING_chapter_1.pdf")

    pages = loader.load_and_split()

    embeddings = OllamaEmbeddings(model="llama3")

    db = FAISS.from_documents(pages[18:25], embeddings)
    
    retirver = db.as_retriever()

    docs = retirver.invoke(query)
    
    return docs

# "What algotithm is used to separate spam e-mail?"