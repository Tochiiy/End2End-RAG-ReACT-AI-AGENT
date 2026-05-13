from langchain.agents import create_agent
from config.settings import llm
from tools.search_tools import search_tools
from tools.rag_tool import rag_retrieval_tool

def build_agent(vectorstore=None):
    tools = search_tools.copy()

    if vectorstore:
        rag_tool = rag_retrieval_tool(vectorstore)
        tools.insert(0, rag_tool)

    return create_agent(llm, tools)