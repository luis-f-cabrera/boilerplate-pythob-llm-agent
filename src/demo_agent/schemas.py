"""
schemas.py

This module defines Pydantic models for handling request data and
input validation in Language Model (LLM) agents.

It includes models for request data, search input, and calculator input.
"""

import dataclasses
from enum import Enum

from pydantic import BaseModel, Field, StringConstraints
from typing_extensions import Annotated, Dict, List


class ChatUserEnum(str, Enum):
    """
    Enumeration for types of chat users.

    Attributes:
        ai (str): Represents the AI chat user.
        human (str): Represents the human chat user.
    """

    AI = "ai"
    HUMAN = "human"


@dataclasses.dataclass
class RequestData(BaseModel):
    """
    Model for request data containing input and chat history.

    Attributes:
        input (Annotated[str, StringConstraints]): The input text for the LLM agent.
        chat_history (List[Dict[ChatUserEnum, str]]): The chat historyas a list of dictionaries
            containing user type and message.
    """

    query: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True, to_lower=True, min_length=1, max_length=4096
        ),
    ]
    chat_history: List[Dict[ChatUserEnum, str]] = []


@dataclasses.dataclass
class SearchInput(BaseModel):
    """
    Model for search input data.

    Attributes:
        query (str): The search query.
    """

    query: str = Field(description="should be a search query")


@dataclasses.dataclass
class CalculatorInput(BaseModel):
    """
    Model for calculator input data.

    Attributes:
        a (int): The first number.
        b (int): The second number.
    """

    a: int = Field(description="first number")
    b: int = Field(description="second number")
