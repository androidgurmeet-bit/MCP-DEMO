
from typing import List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather_server")

@mcp.tool()
def get_weather(location: str) -> str:
    """ Get the current weather for a given location."""
    # In a real implementation, you would call a weather API here.
    return f"The current weather in {location} is sunny with a high of 25°C."   


if __name__ == "__main__":
    mcp.run(transport="stdio")