# Generative AI & LangChain practice (Under development)

## Technologies used:

OpenAI APIs
LangChain
Streamlit
FAISS
SerpAPI

---

project in inception phase:
feed some pdf file and then ask question

equity research tool:
feed some articles and then start asking question about that topic

---

completed projects:
1 - food menu name generator:
where you pick a cuisine and it will create the restaurant name and the list of the menu

2 - Mini LLM Model with URLs
you can list a few URLs and then ask about ask question about the topics that URLs are about.

3 - Question and Answer project
Answering the question based on given context

4 - ask question from database
in this database I use GooglePalm and the following package:
SQLDatabase, SQLDatabaseChain
where you can ask question and the model formulate the sql query to extract the information. and also doing a fast training on the queries that it got wrong (shot learning)
Creating Semantic Similarity Based example selector
create embedding on the few_shots
Store the embeddings in Chroma DB
Retrieve the the top most Semantically close example from the vector store
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

---

disclaimer:
part of the code is written (inspired from) while following/watching some courses from different sources and also some part of the code is copied from stackoverflow.
