import sys
import asyncio
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("aggregator_server")

# Math tools
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@mcp.tool()
def multiple(a: int, b: int) -> int:
    """Multiply two numbers together."""
    return a * b

# Weather tools
@mcp.tool()
def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
    return f"The current weather in {location} is sunny with a high of 25°C."

if __name__ == "__main__":
    mcp.run(transport="stdio")
