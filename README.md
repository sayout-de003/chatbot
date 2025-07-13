Sure! Below is a complete, professional documentation for your **FastAPI + Pinecone-based Document ChatBot**, covering:

* 📁 Directory structure
* 🛠️ Tech stack
* 📄 Step-by-step installation & setup
* 🚀 Run instructions
* 🧠 Internal workflow
* 🧪 Testing the bot
* 📦 Future improvements

---

# 🧠 DocChatBot – Chat with Your Documents

Interact with your documents using natural language, powered by **FastAPI**, **SentenceTransformers**, and **Pinecone**.

---

## 📁 Project Directory Structure

```
docChatBot/
│
├── app/
│   └── embedder.py            # Embedding logic & Pinecone upsert/query
│
├── static/                    # (Optional) static files for frontend
│
├── templates/                 # HTML templates (if using FastAPI + Jinja2)
│   └── index.html
│
├── web_ui.py                  # FastAPI web server & endpoints
├── main.py                    # (Optional, entry point if needed)
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (API keys etc.)
├── README.md                  # Documentation
└── .dcb/                      # Virtual environment (not tracked in Git)
```

---

## 🛠️ Tech Stack

| Component         | Tool / Library                                 |
| ----------------- | ---------------------------------------------- |
| Language          | Python 3.12                                    |
| Web Framework     | FastAPI                                        |
| Embeddings        | [SentenceTransformers](https://www.sbert.net/) |
| Vector DB         | [Pinecone](https://www.pinecone.io/)           |
| Environment       | `python-dotenv`                                |
| Deployment        | Uvicorn ASGI Server                            |
| Optional Frontend | HTML + JS + Jinja2 templates                   |

---

## 🚀 Step-by-Step Setup

### 🔧 1. Clone the Repo

```bash
git clone https://github.com/your-username/docChatBot.git
cd docChatBot
```

---

### 🐍 2. Create a Virtual Environment

```bash
python3 -m venv .dcb
source .dcb/bin/activate
```

---

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, create it:

```txt
fastapi
uvicorn
python-dotenv
sentence-transformers
pinecone-client
```

Then:

```bash
pip install -r requirements.txt
```

---

### 🔐 4. Setup Environment Variables

Create a `.env` file:

```ini
PINECONE_API_KEY=your-pinecone-api-key
PINECONE_HOST=your-index-host-url
PINECONE_INDEX_NAME=chatbot
```

> You can find these in your Pinecone project dashboard.

---

### ⚙️ 5. Set Vector Dimension Properly

* Check your Pinecone index dimension.
* Use a compatible model. For example:

| Model Name          | Vector Dim |
| ------------------- | ---------- |      |
| `BAAI/bge-large-en` | 1024       |

Update `.env` or code accordingly.

---

### 🧠 6. Optional: Set CPU if using macOS (M1/M2)

MPS can be slow. In `app/embedder.py`:

```python
self.model = SentenceTransformer(model_name, device="cpu")
```

---

## 🖥️ Running the App

```bash
uvicorn web_ui:app --reload
```

Visit:
📍 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## ⚙️ How It Works – Internal Workflow

### Upload Workflow (`/upload/`)

1. **PDF/Text file is uploaded**
2. File is chunked into sections
3. Each chunk is embedded via `SentenceTransformer`
4. Embeddings + metadata are upserted to Pinecone (`build_index`)

### Query Workflow (`/ask`)

1. User submits a question
2. It's embedded into a vector
3. Top-K similar chunks are retrieved from Pinecone
4. Those are displayed back to the user

---

## 🧪 Testing the Bot


```


```

---

---

## 🧼 Clean Shutdown

When using `--reload`, the server restarts on code change.

To stop cleanly:

```bash
CTRL+C
```

---

## 💡 Troubleshooting



> `Vector dimension  1024`
> 🔧 Solution: Match model vector size with Pinecone index.

---

## 📄 Credits

* Sentence Transformers: [https://www.sbert.net/](https://www.sbert.net/)
* Pinecone: [https://www.pinecone.io/](https://www.pinecone.io/)
* FastAPI: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)


# chatbot
