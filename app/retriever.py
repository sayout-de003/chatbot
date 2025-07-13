from app.embedder import Embedder

class Retriever:
    def __init__(self, embedder: Embedder):
        self.embedder = embedder

    def retrieve(self, query, k=3):
        return self.embedder.search(query, k)
