# 🤖 RAG-Based Customer Support Assistant
### Built with LangGraph & Human-in-the-Loop (HITL)

> Internship Project — Kirthika R S | 2025

---

## 📌 Project Overview

This project is a **Retrieval-Augmented Generation (RAG)** based Customer Support Assistant that:
- Reads a **PDF knowledge base** of FAQs
- Retrieves relevant information using **vector embeddings**
- Generates accurate answers using **Groq LLaMA 3.3 LLM**
- Uses **LangGraph** for intelligent workflow orchestration
- Escalates to a **Human Agent** when the bot cannot answer confidently

---

## 🗂️ Project Structure

```
rag-support-bot/
│
├── data/
│   └── knowledge_base.pdf       # FAQ knowledge base PDF
│
├── vectorstore/                 # FAISS vector index (auto-generated)
│
├── create_pdf.py                # Creates the knowledge base PDF
├── ingest.py                    # Loads PDF, chunks, embeds and stores in FAISS
├── retriever.py                 # Retrieves relevant chunks from FAISS
├── hitl.py                      # Human-in-the-Loop escalation module
├── graph.py                     # LangGraph workflow with nodes and routing
├── main.py                      # Entry point — runs the chatbot
│
├── .env                         # API keys (not uploaded to GitHub)
├── .gitignore                   # Ignores .env and vectorstore
└── README.md                    # Project documentation
```

---

## ⚙️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.9 | Programming Language |
| LangChain | PDF loading, chunking, retrieval |
| FAISS | Vector database for storing embeddings |
| HuggingFace (all-MiniLM-L6-v2) | Embedding model |
| LangGraph | Graph-based workflow orchestration |
| Groq (LLaMA 3.3 70B) | LLM for answer generation |
| FPDF | PDF creation for knowledge base |
| python-dotenv | Environment variable management |

---

## 🚀 How to Run

### Step 1 — Clone the repository
```bash
git clone https://github.com/Kirthika-cse/rag-support-bot.git
cd rag-support-bot
```

### Step 2 — Install dependencies
```bash
pip install langchain langchain-google-genai langgraph langchain-community
pip install faiss-cpu pypdf sentence-transformers fpdf groq python-dotenv
pip install greenlet --only-binary=:all:
```

### Step 3 — Set up API Key
Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get your free Groq API key at: **console.groq.com**

### Step 4 — Create the knowledge base PDF
```bash
python create_pdf.py
```

### Step 5 — Ingest the PDF into vector store
```bash
python ingest.py
```

### Step 6 — Run the chatbot
```bash
python main.py
```

---

## 💬 Sample Interaction

```
==================================================
Welcome to TechCare Customer Support Bot!
==================================================
Type 'quit' to exit

You: How do I reset my password?
Searching knowledge base...
Generating answer...
Bot: To reset your password, go to Settings > Account > Reset Password.
     Enter your registered email and click Send OTP.

--------------------------------------------------

You: I want to file a legal complaint
Searching knowledge base...

==================================================
🚨 ESCALATING TO HUMAN AGENT
==================================================
Customer Query: I want to file a legal complaint
Bot could not answer confidently.
==================================================
Human Agent - Type your response: Please contact our legal team at legal@techcare.com
Bot: Please contact our legal team at legal@techcare.com
```

---

## 🔄 System Workflow

```
User Query
    │
    ▼
Process Node (LangGraph)
    │
    ├── Retrieves context from FAISS
    │
    ▼
Route Decision
    │
    ├── Context found ──────► Answer Node ──► Groq LLM ──► Answer
    │
    └── No context ─────────► Escalate Node ──► Human Agent ──► Answer
```

---

## 📋 Mandatory Concepts Applied

- ✅ **RAG** — PDF loaded, chunked, embedded and retrieved
- ✅ **Vector Database** — FAISS used for storing and searching embeddings
- ✅ **LangGraph** — Graph-based workflow with 3 nodes and conditional routing
- ✅ **Customer Support Bot** — FAQ-based assistant for SmartHome App
- ✅ **HITL** — Human escalation when bot confidence is low

---

## 📁 Deliverables

| Document | Description |
|---|---|
| HLD Document | High-Level System Architecture Design |
| LLD Document | Low-Level Module and Workflow Design |
| Technical Documentation | Complete technical explanation of the system |
| Working Project | Fully functional RAG chatbot |

---

## 🔮 Future Enhancements

- Multi-document support (multiple PDFs)
- Web interface using FastAPI + Streamlit
- Conversation memory for follow-up questions
- Feedback loop to improve knowledge base
- Docker containerization and cloud deployment

---

## 👩‍💻 Author

**Kirthika R S**
Internship Project — 2025

---

## 📄 License

This project is built for internship/educational purposes.
