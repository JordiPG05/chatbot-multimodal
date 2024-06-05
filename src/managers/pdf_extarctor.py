from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

class PDFExtractor:
    def __init__(self):
        """
        Initializes a new instance of the class.

        This constructor initializes the object with the following attributes:
        - loader: A PyPDFLoader object that loads and splits the PDF file located at "src/data/DEEP_LEARNING_chapter_1.pdf".
        - pages: A list of pages extracted from the PDF file.
        - embeddings: An OllamaEmbeddings object that uses the "llama3" model for embedding.
        - db: A FAISS object that creates a vector store from the specified documents and embeddings.
        - retirver: A retriever object that uses the FAISS vector store for retrieval.

        Parameters:
        None

        Returns:
        None
        """
        self.loader = PyPDFLoader("src/data/DEEP_LEARNING_chapter_1.pdf")

        self.pages = self.loader.load_and_split()

        self.embeddings = OllamaEmbeddings(model="llama3")

        self.db = FAISS.from_documents(documents=self.pages[18:25],
                                embedding=self.embeddings)
        
        self.retirver = self.db.as_retriever()


    def extract_pdf(self,query):
        """
        Retrieves documents from the PDF vector store based on the given query.

        Args:
            query (str): The query to search for in the PDF vector store.

        Returns:
            list: A list of documents retrieved from the PDF vector store.
        """
        # Invoke the retriever object to retrieve documents based on the query
        docs = self.retirver.invoke(query)
        
        return docs


# "What is figure 1.1?"
# "what is this book about?"