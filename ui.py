import streamlit as st
import os
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

# Configuration de la page
st.set_page_config(page_title="LexiRAG", layout="wide")

st.title("📚 Chat avec mes documents")
st.markdown("Posez une question sur vos PDF (George Orwell 1984, etc.)")

# Initialisation du moteur (en cache pour éviter de recharger à chaque clic)
@st.cache_resource
def init_rag():
    store = FaissVectorStore("faiss_store")
    if os.path.exists("faiss_store/faiss.index"):
        store.load()
    else:
        st.error("Index FAISS introuvable ! Lancez app.py d'abord pour indexer vos PDF.")
    return RAGSearch()

rag_search = init_rag()

# Interface utilisateur
query = st.text_input("Votre question :", placeholder="Ex: Que fait Winston dans la boutique ?")

if st.button("Rechercher et Résumer"):
    if query:
        with st.spinner("L'IA analyse vos documents..."):
            # Lancement de la recherche
            summary = rag_search.search_and_summarize(query, top_k=3)
            
            # Affichage du résultat
            st.subheader("Résumé de l'IA")
            st.write(summary)
            
            # Optionnel : Afficher les sources
            with st.expander("Voir les extraits sources"):
                results = rag_search.vectorstore.query(query, top_k=3)
                for res in results:
                    st.info(f"Source : {res['metadata'].get('text', 'Texte inconnu')[:200]}...")
    else:
        st.warning("Veuillez entrer une question.")