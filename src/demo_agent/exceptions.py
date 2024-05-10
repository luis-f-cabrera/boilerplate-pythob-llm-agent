"""
exceptions.py

This module provides exception handling functions for Language Model (LLM) agents.

It includes functions to handle specific types of errors that may occur
during tool execution or HTTP requests.
"""

from langchain_core.tools import ToolException


def _handle_tool_error(error: ToolException) -> str:
    """
    Handle errors that occur during tool execution.

    Parameters:
        error (ToolException): The exception object containing details about the error.

    Returns:
        str: A formatted error message indicating the occurred errors during tool execution.
    """
    return (
        "The following errors occurred during tool execution: "
        + error.args[0]
        + ". Please try another tool."
    )
