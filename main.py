import asyncio
import os
import sys
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

load_dotenv()

#llm = ChatOpenAI(model="gpt-4", temperature=0.7)
llm = ChatOllama(model = "qwen3:1.7b", temperature=0.7)

stdio_server_params = StdioServerParameters(
    command="python",
    args=["/Users/gurmeetsingh/python_demo/LangChain-AgenticAI/mcp-crash-course/servers/aggregator_server.py"],
)

async def main():
    # Redirect debug prints to stderr to avoid contaminating stdout (JSONRPC channel)
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
           await session.initialize()
           sys.stderr.write("Session initialized with MCP servers.\n")
           tools = await load_mcp_tools(session)
           sys.stderr.write(f"Available tools: {tools}\n")
           agent = create_agent(model=llm, tools=tools)

           result = await agent.ainvoke({"messages": [HumanMessage(content="What is the weather like in New York and what is 5 + 7?")]})
           print(result["messages"][-1].content)
           
           
if __name__ == "__main__":
    asyncio.run(main())
