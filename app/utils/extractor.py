from pypdf import PdfReader

def extract_content(path:str) -> str:
    reader = PdfReader(path)
    text = ""
    for pages in reader.pages:
        text += pages.extract_text()
    return text

