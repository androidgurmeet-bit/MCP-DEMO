import asyncio
import os
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent

load_dotenv()

llm = ChatOpenAI(model="gpt-4", temperature=0.7)
stdio_server_params = StdioServerParameters(
    command= "python",
    args=["/Users/gurmeetsingh/python_demo/LangChain-AgenticAI/mcp-crash-course/servers/weather_server.py", "/Users/gurmeetsingh/python_demo/LangChain-AgenticAI/mcp-crash-course/servers/math_server.py"],
)


async def main():
    print("Hello from mcp-crash-course!")
    print("os.getenv('OPENAI_API_KEY'):", os.getenv("OPENAI_API_KEY"))


if __name__ == "__main__":
    asyncio.run(main())
