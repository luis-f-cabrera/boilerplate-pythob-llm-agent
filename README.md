# Boilerplate Python LLM Agent

This boilerplate provides a standardized development environment for creating Language Model (LLM) agents using Python..

## Folder Structure

```
boilerplate-python-lmm-agent
├── src
│   ├── demo_agent
│   │   ├── __init__.py          # Package initialization
│   │   ├── config.py            # Configuration settings
│   │   ├── constants.py         # Constants used throughout the application
│   │   ├── dependencies.py      # Dependency definitions
│   │   ├── exceptions.py        # Custom exception definitions
│   │   ├── llm_agent.py         # Function to run a Language Model Agent (LLM)
│   │   ├── llm_prompts.py       # Templates for LLM prompts
│   │   ├── llm_tools.py         # Tools for interacting with the LLM
│   │   ├── router.py            # FastAPI router for handling requests
│   │   ├── schemas.py           # Pydantic schemas for request/response validation
│   ├── __init__.py               # Package initialization
│   ├── main.py                   # Instance of the FastAPI APP for local development
├── tests/
├── .env                         # Environment variables configuration
├── .gitignore                   # Defines which files to ignore in Git
├── .pre-commit-config.yaml      # Configuration for pre-commit hooks
├── .python-version              # Specifies the Python version to use
├── Makefile                     # Commands for managing the project
├── poetry.lock                  # Lock file for Poetry dependencies
├── pyproject.toml               # Project metadata and dependencies defined using Poetry
└── README.md                    # Instructions for using the repository

```

# Usage

## Makefile Commands

- **install**: Installs project dependencies.
- **activate**: Activates the virtual environment.
- **clean**: Cleans the environment and hooks.
- **run**: Runs the FastAPI app locally.

To use these commands, simply navigate to the root directory of your project in the terminal and run `make <command>`.

# Getting Started

## Installation

To get started with the boilerplate, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone <repository_url>
```

2. Navigate to the project directory:

```bash
cd boilerplate-python-lmm-agent
```

3. Install project dependencies using the following command:

```bash
make install
```

This will install all the necessary dependencies for the project.

## Activation

After installing the dependencies, activate the virtual environment using the following command:

```bash
make activate
```

This will activate the virtual environment, allowing you to work within an isolated environment with all project dependencies available.

## Running the Application

To run the FastAPI application locally, use the following command:

```bash
make run
```

This will start the FastAPI server, allowing you to access the endpoints locally at `http://localhost:8080`.

## Modifying the LLM Agent

To create a custom LLM agent, you can modify the `llm_agent.py` file and other relevant files within the `src/demo_agent` directory.

- **llm_agent.py**: This file contains the function to run the Language Model (LLM) agent. You can modify this file to customize the behavior of your LLM agent.

- **schemas.py**: This file contains Pydantic schemas for request and response validation. You can define the structure of the data expected by your LLM agent and the format of the response it generates.

- **constants.py**: This file contains constants used throughout the application. You can define any constants or configuration settings relevant to your LLM agent in this file.

- **llm_prompts.py**: This file contains templates for LLM prompts. You can define different prompts to interact with your LLM agent based on specific use cases or scenarios.


# References

- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction): Official documentation for LangChain, providing comprehensive guidance on getting started with language models and related tools.

- [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices?tab=readme-ov-file#7-dont-make-your-routes-async-if-you-have-only-blocking-io-operations): A GitHub repository containing best practices for building APIs with FastAPI. This resource offers valuable insights into optimizing and structuring FastAPI applications for better performance and maintainability.
