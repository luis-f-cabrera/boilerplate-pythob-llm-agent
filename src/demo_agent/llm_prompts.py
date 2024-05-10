"""
llm_prompts.py

This module provides prompt templates for Language Model (LLM) agents.

It contains predefined templates that are used to structure conversations
between the LLM agent and users.
"""

PROMPT = """
SYSTEM: You are a helpful assistant
{chat_history}
human: {input}
{agent_scratchpad}
"""
