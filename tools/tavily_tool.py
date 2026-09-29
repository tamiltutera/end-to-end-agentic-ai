from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()

client = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))

def tavily_search(query: str, limit: int = 5):
    """
    Search for a query using Tavily API.

    Args:
        query (str): The search query.
        limit (int): The maximum number of results to return.
    """
    response = client.search(query, max_results=limit)
    results = []
    for i, r in enumerate(response["results"], 1):
        title = r.get("title", "No title")
        url = r.get("url", "No URL")
        snippet = r.get("snippet", "No snippet")

        if len(results) < 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..." 
            results.append(f"{i}. {title}\nURL: {url}\nSnippet: {snippet}\n")
    return "\n\n".join(results)