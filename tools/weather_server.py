from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather_api")
@mcp.tool()
async def get_weather(location : str):
    """Weather API to search about real time weather."""
    return "Weather is Good"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")