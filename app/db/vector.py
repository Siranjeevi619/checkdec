from langchain_chroma import Chroma
from app.embeddings.embedding import chunks, embeddings

chroma_db = Chroma.from_texts(embedding=embeddings,
                              text = chunks,
                              persist_directory='./chroma_db')

