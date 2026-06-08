import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import mcp  
load_dotenv()  # Load environment variables from .env file


llm = ChatOpenAI(model="gpt-4", temperature=0.7)

async def main():
    print("Hello from the LangChain MCP Client!")
    
if __name__ == "__main__":
        asyncio.run(main())