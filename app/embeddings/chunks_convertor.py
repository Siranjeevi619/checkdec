from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
def chunk_convertor(resume_content : str) -> List[any]:
    splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
    chunks = splitter.split_text(resume_content)
    print(type(chunks))
    return chunks 