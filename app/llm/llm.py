from app.utils.config import config
from app.prompts.prompt import prompt


from langchain_ollama import ChatOllama

model = ChatOllama(model = 'gemma4', temperature=0.5)

llm = prompt | model

response = llm.invoke(
    "What is your parameter size?"
)

print (response.content)