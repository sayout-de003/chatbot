import sys
from dotenv import load_dotenv
from app.ingestion import load_documents, split_documents
from app.embedder import Embedder
from app.retriever import Retriever
from app.qa_chain import QAGenerator

def run_cli(folder_path):
    print(f"[INFO] Loading and processing documents from '{folder_path}'...")
    docs = load_documents(folder_path)
    chunks = split_documents(docs)

    embedder = Embedder()
    embedder.build_index(chunks)
    retriever = Retriever(embedder)
    qa = QAGenerator()

    print("\n[READY] Ask questions (type 'exit' to quit):")
    while True:
        query = input("Q: ")
        if query.lower() == 'exit':
            break
        results = retriever.retrieve(query)
        context = "\n\n".join([r['text'] for r in results])
        answer = qa.generate_answer(query, context)
        print(f"\nA: {answer}")
        print("Sources:", [f"{r['metadata']['source']}, chunk {r['metadata']['chunk']}" for r in results])

if __name__ == "__main__":
    load_dotenv()
    path = sys.argv[1] if len(sys.argv) > 1 else "docs"
    run_cli(path)
