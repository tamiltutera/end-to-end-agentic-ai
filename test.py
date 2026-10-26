import asyncio
from mcp_client_test import get_all_tools, tavily_mcp_search

async def main():
    await get_all_tools()
    result = await tavily_mcp_search("Python programming")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())