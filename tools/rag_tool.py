from langchain_core.tools import create_retriever_tool
def rag_retrieval_tool(vectorstore):
    retriever = vectorstore.as_retriever()
    return create_retriever_tool(
        retriever,
        name="document_search",
        description="Search uploaded documents for relevant information.",
    )