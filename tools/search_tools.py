from langchain_tavily import TavilySearch
from langchain_community.tools import DuckDuckGoSearchRun

tavily_tool = TavilySearch(max_results=2)
ddg_tool    = DuckDuckGoSearchRun()

search_tools = [tavily_tool, ddg_tool]