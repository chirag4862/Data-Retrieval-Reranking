# Data Retrieval and Reranking API

<div align="center">
<a href="https://twitter.com/jaadui_chirag" target="_blank">
<img src=https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white alt=twitter style="margin: 0 5px 5px 0;" />
</a>
<a href="https://linkedin.com/in/chirag-vijay-b55b361a5" target="_blank">
<img src=https://img.shields.io/badge/linkedin-%231E77B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white alt=linkedin style="margin: 0 5px 5px 0;" />
</a>
<a href="https://hashnode.com/@chirag4862" target="_blank">
<img src=https://img.shields.io/badge/hashnode-%232962FF.svg?&style=for-the-badge&logo=hashnode&logoColor=white alt=hashnode style="margin: 0 5px 5px 0;" />
</a>
<a href="https://medium.com/@jaadui_chirag" target="_blank">
<img src=https://img.shields.io/badge/medium-%23292929.svg?&style=for-the-badge&logo=medium&logoColor=white alt=medium style="margin: 0 5px 5px 0;" />
</a>  
</div>

## About

This project provides an API for **Data Retrieval and Reranking** built using Python Flask. It allows for semantic search and retrieval of data from encoded documents stored in a vector database. The API utilizes a bi-encoder for dense retrieval and a cross-encoder for reranking to provide the most optimal search results.

The primary use case is to upload PDF documents, encode them, store the vectors in a database, and enable a query-based search system that ranks the most relevant results. This system builds on the foundational ideas from the [Sentence Transformers Retrieve & Re-Rank Example](https://sbert.net/examples/applications/retrieve_rerank/README.html), but provides an upgraded, more efficient implementation.

## Features

- **PDF Document Ingestion**: Upload a PDF document and store its encoded form in a vector database.
- **Semantic Search**: Retrieve and rerank documents based on the relevance of the search query.
- **Cross-Encoding**: Enhance the precision of results using a cross-encoder for reranking.
- **Vector Database**: Efficiently store and query encoded data using semantic vector search.

## Dependencies

To run the API, the following dependencies are required:

- `Flask`
- `PyPDF2`
- `SentenceTransformer`
- `rank_bm25`
- `sklearn`
- `tqdm`
- `chromadb`

You can install the dependencies using the following command:

```bash
pip install Flask PyPDF2 sentence-transformers rank-bm25 scikit-learn tqdm chromadb
```

## How to Use

### 1. Run the Application

To start the API on your local system, run the following command:

```bash
python app.py
```

### 2. API Endpoints

- **Create Collection**  
  Upload a PDF document, encode it, and store it in a new collection in the vector database.

  **Endpoint:**

  ```bash
  POST /create/<file_path>/<collection_name>
  ```

  **Example:**

  ```bash
  POST /create/my_document.pdf/my_collection
  ```

- **Query Collection**  
  Perform a semantic search on a collection using a user query. The system will return the top 3 most relevant results after reranking.

  **Endpoint:**

  ```bash
  GET /query/<user_query>/<collection_name>
  ```

  **Example:**

  ```bash
  GET /query/what is artificial intelligence/my_collection
  ```

- **Get Collection Names**  
  Retrieve all the collection names currently present in the vector database.

  **Endpoint:**

  ```bash
  GET /collections/
  ```

## Example Workflow

1. **Ingest Document**: Upload a PDF document and create a collection for it.

   ```bash
   POST /create/Anime.pdf/Anime
   ```

2. **Perform Search**: Query the collection for relevant documents.

   ```bash
   GET /query/When was the first anime created/Anime
   ```

3. **Retrieve Collections**: List all the current collections in the database.
   ```bash
   GET /collections/
   ```

## Contribution

We welcome contributions from the community to enhance and improve this project. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch and open a pull request with a description of the changes.

### Guidelines

- Please ensure that your code follows the best practices for Python and is well-documented.
- Ensure all tests pass before submitting your pull request.
- Describe your changes in detail and reference any related issues.
