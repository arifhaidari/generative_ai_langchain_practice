# Generative AI, LangChain and LMM (Practices)

This repository hosts a series of projects to practice and experiment with **Generative AI** and **LangChain**, integrating various tools and APIs to build intelligent applications for data generation, question-answering, and more. These projects help enhance understanding of language models and frameworks by applying them to real-world scenarios.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Project Overview](#project-overview)
  - [Inception Phase](#inception-phase)
  - [Completed Projects](#completed-projects)
- [How to Run the Projects](#how-to-run-the-projects)
- [Future Enhancements](#future-enhancements)
- [Disclaimer](#disclaimer)

---

## Technologies Used

- **LangChain**: Framework for building applications with language models.
- **python-dotenv**: To manage environment variables securely.
- **OpenAI API**: Core language model used for text generation and question answering.
- **LangChain Community Tools**: Additional components for advanced language chain functionalities.
- **Streamlit**: Framework for creating interactive web applications.
- **sentence-transformers**: Library for generating and working with sentence embeddings.
- **FAISS**: A library for efficient similarity search and clustering of dense vectors.
- **SerpAPI**: API for fetching Google search results for specific queries.
- **Unstructured**: Library for processing and transforming unstructured data like PDFs and text.
- **Tiktoken**: Efficient tokenization library used in conjunction with OpenAI models.
- **HuggingFace Transformers**: To implement various models for tasks like embedding creation.
- **Google Palm**: For language and database query integration.
- **Chroma DB**: Vector database for storing and retrieving embeddings.

---

## Project Overview

### Inception Phase

- **PDF Question Answering Tool**:

  - **Description**: Feed PDF documents into the system and ask questions about the content. The model retrieves answers based on the ingested files, making it useful for research, legal document analysis, or academic reading.
  - **Tools Used**: LangChain, OpenAI, Unstructured for PDF processing.

- **Equity Research Tool**:
  - **Description**: This tool processes financial articles related to equity research. Users can ask questions regarding stocks, market trends, or specific companies, and the model will retrieve and analyze the relevant data.
  - **Tools Used**: OpenAI API, SerpAPI for gathering articles, LangChain.

---

### Completed Projects

1. **Food Menu Name Generator**:

   - **Description**: Select a cuisine type, and the tool generates a restaurant name and a corresponding menu, showcasing creative text generation using AI.
   - **Tools Used**: OpenAI API, LangChain, Streamlit for web UI.

2. **Mini LLM Model with URLs**:

   - **Description**: Users provide a list of URLs, and the system scrapes content from them. The user can then ask questions about the topics the URLs cover. This demonstrates the use of web scraping and natural language understanding.
   - **Tools Used**: OpenAI API, LangChain, SerpAPI for URL content extraction.

3. **Question and Answer (QA) Project**:

   - **Description**: A simple system that allows users to ask questions based on provided context. Ideal for studying or training models on specific data.
   - **Tools Used**: OpenAI API for question generation and response formulation.

4. **Database Query Tool (SQL Questioning System)**:

   - **Description**: This tool uses Google Palm and LangChain’s SQLDatabase integration to allow users to ask questions about a database. It converts questions into SQL queries, executes them, and returns relevant information from the database.
   - **Features**:
     - Short-term training on misinterpreted queries.
     - Embedding-based query similarity selector using HuggingFace models.
     - Embeddings stored in **Chroma DB** for efficient retrieval.
     - **Tools Used**: Google Palm, SQLDatabaseChain, HuggingFace Embeddings, Chroma DB.

   ```python
   from langchain.prompts import SemanticSimilarityExampleSelector
   from langchain.embeddings import HuggingFaceEmbeddings
   from langchain.vectorstores import Chroma

   embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
   ```

---

## How to Run the Projects

1. Clone the repository:

   ```bash
   git clone https://github.com/arifhaidari/generative_ai_langchain_practice.git
   cd generative_ai_langchain_practice
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run each project as follows:

   - For example, to run the **Food Menu Name Generator**:
     ```bash
     cd food-menu-generator
     streamlit run app.py
     ```

4. Additional instructions for other projects are provided in their respective directories.

---

## Future Enhancements

- **Advanced RAG (Retrieval-Augmented Generation)**: Implement retrieval-augmented pipelines to enhance contextual understanding in QA tools.
- **Embeddings from Diverse Sources**: Experiment with embedding models like **OpenAI Embeddings** and **Cohere** to optimize search accuracy.
- **User Interface Improvements**: Further develop the front-end for better user experience, potentially moving beyond **Streamlit** to more advanced frameworks like **React**.
- **Integration of Multimodal Models**: Extend current projects to include text, image, and video inputs.

---

## Disclaimer

This project is a mix of original work and code inspired by tutorials, courses, and contributions from platforms like StackOverflow. Credit is given to the respective authors where applicable.
