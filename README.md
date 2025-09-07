# MCP (Multi-Server Client-Provider)

This repository contains a Python library that enables interaction with multiple server back‑ends (e.g., local Python tools, HTTP services) through a unified **Multi‑Server MCP Client**.

## Features

- **Multi‑Server Support** – Define a dictionary of servers (e.g., a math tool, a weather HTTP service) and the client will automatically expose them as LangChain tools.
- **Transport Abstractions** – Supports `stdio` for local command‑line tools and `streamable_http` for HTTP endpoints.
- **LangChain Integration** – Seamlessly works with LangChain agents such as the `create_react_agent` from `langgraph`.
- **Async Ready** – All operations are asynchronous, allowing non‑blocking calls in agent workflows.

## Quick Start

```python
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
import asyncio, os

async def main():
    client = MultiServerMCPClient({
        "math": {
            "command": "python",
            "args": ["tools/maths_server.py"],
            "transport": "stdio",
        },
        "weather": {
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http",
        },
    })

    tools = await client.get_tools()
    model = ChatGroq(model="qwen/qwen3-32b")
    agent = create_react_agent(model, tools)

    # Example math query
    math_res = await agent.ainvoke({"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]})
    print(math_res['messages'][-1].content)

    # Example weather query
    weather_res = await agent.ainvoke({"messages": [{"role": "user", "content": "what is the weather in California?"}]})
    print(weather_res['messages'][-1].content)

asyncio.run(main())
```

## Repository Structure

- `client.py` – Implements the `MultiServerMCPClient` that discovers and wraps server tools.
- `main.py` – Example entry point demonstrating usage.
- `tools/` – Directory for custom tool scripts (e.g., `maths_server.py`).
- `requirements.txt` / `pyproject.toml` – Project dependencies.

## License

MIT License – feel free to use, modify, and distribute.
