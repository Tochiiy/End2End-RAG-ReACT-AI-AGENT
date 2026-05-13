import time
from langchain_core.messages import HumanMessage

def retry(agent, query, retries=3, wait=30):
    for i in range(retries):
        try:
            result = agent.invoke({
                "messages": [HumanMessage(content=query)]
            })
            return result["messages"][-1].content
        except Exception as e:
            if "429" in str(e) or "rate" in str(e).lower():
                print(f"Rate limited. Waiting {wait}s... ({i+1}/{retries})")
                time.sleep(wait)
            else:
                return f"Error: {str(e)}"
    return "Max retries exceeded."