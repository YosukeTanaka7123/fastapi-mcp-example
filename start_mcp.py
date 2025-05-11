from app.main import app
from fastapi_mcp import FastApiMCP

# Add MCP server to the FastAPI app
mcp = FastApiMCP(app)

# Mount the MCP server to the FastAPI app
mcp.mount()
