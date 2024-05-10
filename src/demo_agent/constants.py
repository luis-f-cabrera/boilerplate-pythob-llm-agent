"""
constants.py

This module houses essential constants utilized by Language Model (LLM) agents.

Included are settings such as the agent's name, default router response,
model parameters, as well as business constants and dictionaries.
"""

# Default agent name
AGENT_NAME = "demo_agent"

# Default router response for HTTP 404 Not Found
router_default_response = {404: {"description": "Not found"}}

# Model parameters
MODEL = "gpt-4-1106-preview"
TEMPERATURE = 0
MAX_ITERATIONS = 5
VERBOSE = True
RETURN_ONLY_OUTPUTS = True
