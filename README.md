## LexiRAG (RAG Pipeline)

Ce projet est une implémentation d'un système **RAG (Retrieval-Augmented Generation)** permettant d'indexer des documents PDF locaux et d'interroger leur contenu de manière intelligente grâce à l'intelligence artificielle.

<img width="1254" height="558" alt="image" src="https://github.com/user-attachments/assets/597920bd-316b-4b3b-8f0d-94bb3a171fef" />

### Fonctionnalités

* **Ingestion de PDF** : Chargement récursif de documents depuis un dossier local.
* **Découpage Intelligent (Chunking)** : Utilisation de `RecursiveCharacterTextSplitter` pour préserver la cohérence des phrases.
* **Embeddings sémantiques** : Conversion du texte en vecteurs mathématiques via le modèle `all-MiniLM-L6-v2`.
* **Base de données Vectorielle** : Stockage persistant avec **ChromaDB** pour des recherches ultra-rapides.
* **Interface web** : Chat avec une interface web fait avec **Streamlit**.


### Architecture du Projet

Le système suit le flux de traitement suivant :


1.  **Chargement** : Les fichiers PDF sont lus page par page.
2.  **Découpage** : Le texte est divisé en morceaux de 1000 caractères avec un recouvrement (overlap) de 200 pour garder le contexte.
3.  **Vectorisation** : Chaque morceau est transformé en un vecteur de **384 dimensions**.
4.  **Stockage** : Les vecteurs et métadonnées sont sauvegardés dans une collection ChromaDB.


### Pou lancer le projet

  ```bash
  streamlit run ui.py
```
