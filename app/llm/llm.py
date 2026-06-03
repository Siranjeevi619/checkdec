from app.utils.config import config
from app.prompts.job_selector import prompt
from app.embeddings.embedding import extract_content

from langchain_ollama import ChatOllama

model = ChatOllama(model = config.model_name, temperature=0.5)

llm = prompt | model


resume_content = extract_content('./app/resume/Siranjeevi_v1_2p.pdf')

response = llm.invoke(resume_content)

print (response.content)