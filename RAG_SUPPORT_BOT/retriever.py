from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_retriever():
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )
    return retriever

def retrieve_docs(query):
    retriever = get_retriever()
    docs = retriever.invoke(query)
    context = "\n".join([doc.page_content for doc in docs])
    return context

if __name__ == "__main__":
    query = "How do I reset my password?"
    result = retrieve_docs(query)
    print("Retrieved Context:")
    print(result)