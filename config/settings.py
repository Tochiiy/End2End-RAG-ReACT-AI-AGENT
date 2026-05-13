from dotenv import load_dotenv
import os

load_dotenv()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    model="openrouter/free" 
)