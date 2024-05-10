"""
main.py

This module initializes the FastAPI application and includes routers for different
components of the LLM agent.

It creates a FastAPI instance with configurable settings based on the environment
specified in the `.env` file.
"""

import os

from fastapi import FastAPI
from starlette.config import Config

from src.demo_agent.router import router as demo_agent_router

config = Config(".env")  # Parse .env file for environment variables
ENVIRONMENT = os.getenv("ENVIRONMENT", None)
SHOW_DOCS_ENVIRONMENT = (
    "local",
    "staging",
)  # List of environments where docs should be shown

app_configs = {"title": "agent_api"}
if ENVIRONMENT not in SHOW_DOCS_ENVIRONMENT:
    app_configs[
        "openapi_url"
    ] = None  # Set URL for docs as null if not in allowed environments

app = FastAPI(**app_configs)

# Includes the router for the demo agent component
app.include_router(demo_agent_router)
