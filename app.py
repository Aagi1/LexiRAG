from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch
import os

FAISS_INDEX_PATH = "faiss_store/faiss.index"

# Example usage
if __name__ == "__main__":
    
    
    store = FaissVectorStore("faiss_store")

    if not os.path.exists("faiss_store/faiss.index"):
        print("[INFO] Index non trouvé. Construction initiale...")
        docs = load_all_documents("data")
        store.build_from_documents(docs)
    else:
        print("[INFO] Index existant détecté. Chargement immédiat...")
        store.load()

    rag_search = RAGSearch()
    query = "Winston examina la petite pièce miteuse au-dessus de la boutique"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)
