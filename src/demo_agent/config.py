"""
config.py

This module manages the configuration settings required for Language Model (LLM) agents.

It handles the retrieval of environment variables necessary for seamless interaction
with OpenAI services.
"""

import os

from dotenv import load_dotenv

load_dotenv(override=True)

# Retrieve OpenAI base URL and API key from environment variables
openai_base_url = os.getenv("OPENAI_BASE_URL", None)
openai_api_key = os.getenv("OPENAI_API_KEY", None)
