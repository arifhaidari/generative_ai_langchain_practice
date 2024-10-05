import os
import streamlit as st
import pickle
import time
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain.vectorstores import FAISS

load_dotenv()  

st.title("Mini LLM With URLs")
st.sidebar.title("List of URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"Article {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process Articles")
file_path = "mini_llm_vector.pkl"

main_placeholder = st.empty()
llm = OpenAI(temperature=0.9, max_tokens=500)

if process_url_clicked:
     # load data
     loader = UnstructuredURLLoader(urls=urls)
     main_placeholder.text("Processing the data")
     data = loader.load()
     # split data
     text_splitter = RecursiveCharacterTextSplitter(
          separators=['\n\n', '\n', '.', ','],
          chunk_size=1000
     )
     main_placeholder.text("Splitting the text")
     docs = text_splitter.split_documents(data)
     # create embeddings and save it to FAISS index
     embeddings = OpenAIEmbeddings()
     # Faiss: A library for efficient similarity search
     vectorstore_openai = FAISS.from_documents(docs, embeddings)
     main_placeholder.text("Vector Embedding started")
     time.sleep(2)

     # Save the FAISS index to a pickle file
     with open(file_path, "wb") as f:
          pickle.dump(vectorstore_openai, f)

query = main_placeholder.text_input("Question: ")
if query:
     if os.path.exists(file_path):
          with open(file_path, "rb") as f:
               vectorstore = pickle.load(f)
               chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
               result = chain({"question": query}, return_only_outputs=True)
               # result will be a dictionary of this format --> {"answer": "", "sources": [] }
               st.header("Answer")
               st.write(result["answer"])

               # Display sources, if available
               sources = result.get("sources", "")
               if sources:
                    st.subheader("Sources:")
                    sources_list = sources.split("\n")  # Split the sources by newline
                    for source in sources_list:
                         st.write(source)



