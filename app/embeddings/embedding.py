from app.utils.extractor import extract_content
from app.embeddings.chunks_convertor import chunk_convertor
from app.utils.config import config
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
content = extract_content("./app/resume/Siranjeevi_v1_2p.pdf")

chunks = chunk_convertor(resume_content = content)
embeddings = HuggingFaceEmbeddings(model_name = config.embedding_model_name)
