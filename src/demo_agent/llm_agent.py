"""
llm_agent.py

This module defines a function to run a language model agent (LLM)
for generating responses based on input and chat history.
"""

from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from .constants import MODEL, RETURN_ONLY_OUTPUTS, TEMPERATURE, VERBOSE
from .llm_prompts import PROMPT
from .llm_tools import CustomCalculatorTool, CustomSearchTool, TavilySearchCustomTool


def run_agent(
    query,
    chat_history,
) -> str:
    """
    Run the language model agent to generate a response based on the input and chat history.

    Parameters:
        query (str): The input text to the agent.
        chat_history (str): The chat history as context for generating the response.

    Returns:
        str: The generated response by the agent.
    """
    # Initialize the ChatOpenAI model with specified parameters
    llm = ChatOpenAI(model=MODEL, temperature=TEMPERATURE)

    # Initialize custom tools for the agent
    tools = [CustomSearchTool(), CustomCalculatorTool(), TavilySearchCustomTool()]

    # Initialize the prompt template
    prompt = PromptTemplate.from_template(PROMPT)

    # Create the LLM agent with specified tools and prompt
    agent = create_openai_tools_agent(llm, tools, prompt)

    # Initialize the agent executor with the agent and tools
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=VERBOSE)

    # Invoke the agent with input and chat history, and return only the output
    output = agent_executor.invoke(
        {"input": query, "chat_history": chat_history},
        return_only_outputs=RETURN_ONLY_OUTPUTS,
    )["output"]

    return output
