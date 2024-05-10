"""
llm_tools.py

This module defines custom tools for Language Model (LLM) agents.

It includes tools for custom search and calculator functionalities.
"""

from typing import Type

from langchain.tools import BaseTool
from langchain_community.tools.tavily_search import TavilySearchResults
from pydantic import BaseModel

from .exceptions import _handle_tool_error
from .schemas import CalculatorInput, SearchInput


class CustomSearchTool(BaseTool):  # pylint: disable=too-few-public-methods
    """
    Custom tool for performing search operations.

    Attributes:
        name (str): The name of the tool.
        description (str): Description of the tool.
        args_schema (Type[BaseModel]): Pydantic model for input validation.
        handle_tool_error (function): Function to handle tool errors.
    """

    name = "custom_search"
    description = "Useful for when you need to answer questions about current events"
    args_schema: Type[BaseModel] = SearchInput
    handle_tool_error = _handle_tool_error

    def _run(self) -> str:
        """Use the tool."""
        return "LangChain"

    async def _arun(self) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("Custom search does not support async")


class CustomCalculatorTool(BaseTool):  # pylint: disable=too-few-public-methods
    """
    Custom tool for performing mathematical calculations.

    Attributes:
        name (str): The name of the tool.
        description (str): Description of the tool.
        args_schema (Type[BaseModel]): Pydantic model for input validation.
        handle_tool_error (function): Function to handle tool errors.
    """

    name = "Calculator"
    description = "Useful for when you need to answer questions about math"
    args_schema: Type[BaseModel] = CalculatorInput
    handle_tool_error = _handle_tool_error

    def _run(self, a: int, b: int) -> str:
        """Use the tool."""
        return a * b

    async def _arun(self, a: int, b: int) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("Calculator does not support async")


class TavilySearchCustomTool(
    TavilySearchResults
):  # pylint: disable=too-few-public-methods
    """
    Custom tool for performing Tavily search with specific configurations.

    Attributes:
        handle_tool_error (function): Function to handle tool errors.
        max_results (int): Maximum number of search results.
    """

    handle_tool_error = _handle_tool_error
    max_results = 1
