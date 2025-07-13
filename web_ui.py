from fastapi import FastAPI, UploadFile, File
from app.ingestion import load_documents, split_documents
from app.embedder import Embedder
from app.retriever import Retriever
from app.qa_chain import QAGenerator
import os

app = FastAPI()
embedder = Embedder()
qa = QAGenerator()

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    os.makedirs("temp", exist_ok=True)
    file_path = os.path.join("temp", file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    docs = load_documents("temp")
    chunks = split_documents(docs)
    embedder.build_index(chunks)
    return {"status": "uploaded", "chunks": len(chunks)}

@app.get("/ask/")
def ask(query: str):
    retriever = Retriever(embedder)
    results = retriever.retrieve(query)
    context = "\n\n".join([r['text'] for r in results])
    answer = qa.generate_answer(query, context)
    sources = [f"{r['metadata']['source']} (chunk {r['metadata']['chunk']})" for r in results]
    return {"answer": answer, "sources": sources}
