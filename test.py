from tools.tavily_tool import tavily_search

result = tavily_search("Best hotels in India", limit=5)
print(result)