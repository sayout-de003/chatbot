import os
import uuid
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from pinecone import Pinecone

# Load environment variables
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "chatbot")
HOST = os.getenv("PINECONE_HOST")
DIMENSION = 1024

# Initialize Pinecone client and index
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(host=HOST)

class Embedder:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        model_name = "BAAI/bge-large-en"
        # model_name= "intfloat/e5-base-v2"


        self.model = SentenceTransformer(model_name, device="cpu")

        self.index = index

    def build_index(self, chunks):
        texts = [c['text'] for c in chunks]
        vectors = self.model.encode(texts, show_progress_bar=True)

        upserts = []
        for i, (vector, chunk) in enumerate(zip(vectors, chunks)):
            uid = str(uuid.uuid4())
            metadata = chunk['metadata']
            upserts.append((uid, vector.tolist(), metadata))

        self.index.upsert(vectors=upserts, namespace="default")

    def search(self, query, k=3):
        query_vec = self.model.encode(query).tolist()
        results = self.index.query(
            vector=query_vec,
            top_k=k,
            include_metadata=True,
            namespace="default"
        )

        return [
            {
                "text": match["metadata"].get("text", ""),
                "metadata": match["metadata"]
            }
            for match in results.get("matches", [])
        ]
