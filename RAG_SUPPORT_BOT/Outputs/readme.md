# Output Screenshots

## 1. System Execution and Output

**Screenshot Name:** `system_execution_output.png`

![System Execution Output](screenshots/system_execution_output.png)

**Description:**
This screenshot demonstrates the successful execution of the RAG-Based Customer Support AI Assistant. The user entered the query **"APP IS NOT RESPONDING"** through the command-line interface. The system processed the query using the Retrieval-Augmented Generation (RAG) workflow, retrieved relevant information from the FAISS vector database, and generated a context-aware response using the Groq LLaMA model. This output validates the integration of LangChain, FAISS, LangGraph, and Groq LLaMA for intelligent customer support.

---

## 2. Query Response Generation

**Screenshot Name:** `query_response_generation.png`

![Query Response Generation](screenshots/query_response_generation.png)

**Description:**
This screenshot illustrates the response generation capability of the RAG-Based Customer Support Assistant. When the user entered the query **"WHAT IS THE SUBSCRIPTION PLAN"**, the system searched the knowledge base, retrieved relevant information using semantic similarity search from the FAISS vector database, and generated an accurate response containing available subscription plans and pricing details. This demonstrates effective AI-powered information retrieval and response generation.

---

## 3. Customer Query Handling

**Screenshot Name:** `customer_query_handling.png`

![Customer Query Handling](screenshots/customer_query_handling.png)

**Description:**
This screenshot shows how the system handles customer support issues. The query **"FAMILY MEMBER UNABLE TO CONNECT"** was processed through the RAG pipeline. Relevant troubleshooting information was retrieved from the knowledge base, and the Groq LLaMA model generated detailed guidance, including family sharing settings verification, invitation acceptance procedures, device compatibility checks, and customer support contact recommendations. This demonstrates intelligent customer issue resolution using AI.

---

## 4. Invalid Query Handling

**Screenshot Name:** `invalid_query_handling.png`

![Invalid Query Handling](screenshots/invalid_query_handling.png)

**Description:**
This screenshot demonstrates the system's ability to handle invalid or unclear user queries. When the random text **"KIHBFMJDF"** was entered, the RAG-Based Customer Support Assistant could not identify any meaningful context within the knowledge base. Instead of generating incorrect information, the system produced an appropriate fallback response requesting the user to rephrase the query. This ensures reliable and user-friendly interaction through intelligent query validation.

---

## Summary

The outputs demonstrate the successful implementation of a Retrieval-Augmented Generation (RAG) based Customer Support Assistant using LangGraph, LangChain, FAISS Vector Database, FastAPI, and Groq LLaMA. The system effectively performs semantic retrieval, context-aware response generation, customer issue resolution, and invalid query handling, providing an intelligent AI-powered customer support solution.

