import os
import PyPDF2
import docx2txt
import markdown
from langchain.text_splitter import RecursiveCharacterTextSplitter

SUPPORTED_FORMATS = ('.pdf', '.txt', '.md', '.docx')

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file_path)
        return "\n".join([page.extract_text() for page in reader.pages])
    elif file_path.endswith('.txt'):
        with open(file_path, 'r') as f:
            return f.read()
    elif file_path.endswith('.md'):
        with open(file_path, 'r') as f:
            return markdown.markdown(f.read())
    elif file_path.endswith('.docx'):
        return docx2txt.process(file_path)
    return ""

def load_documents(folder_path):
    docs = []
    for fname in os.listdir(folder_path):
        if fname.endswith(SUPPORTED_FORMATS):
            full_path = os.path.join(folder_path, fname)
            content = extract_text(full_path)
            docs.append({'content': content, 'source': fname})
    return docs

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = []
    for doc in documents:
        splits = splitter.split_text(doc['content'])
        for i, chunk in enumerate(splits):
            chunks.append({
                'text': chunk,
                'metadata': {'source': doc['source'], 'chunk': i, 'text': chunk}
            })
    return chunks
