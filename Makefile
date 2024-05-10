################################################################################
# Makefile
#
# This Makefile provides a set of commands for managing dependencies,
# environment setup, and running the application.
#
# Usage:
#     make install      Install dependencies and set up environment.
#     make activate     Activate virtual environment.
#     make clean        Clean environment and hooks.
#     make run          Run the application.
#
# Commands:
#     - install:       Installs dependencies and sets up the environment,
#                      including creating a virtual environment using Pyenv and Poetry.
#     - activate:      Activates the virtual environment.
#     - clean:         Cleans the environment and hooks.
#     - run:           Runs the application using uvicorn.
#
# Note:
#     This Makefile assumes that a .env file is present in the project directory.
################################################################################

include .env
export

install:
	@echo "Installing dependencies..."
	# Check if .python-version file exists
	python_version=$$(cat .python-version);
	pyenv install $$python_version --skip-existing;
	pyenv local $$python_version;
	curl -sSL https://install.python-poetry.org | python3 - --version 1.7.1;
	poetry install --no-root --sync;

	poetry self add poetry-dotenv-plugin
	poetry run pre-commit install

activate:
	@echo "Activating virtual environment..."
	poetry shell

clean:
	@echo "Cleaning env and hooks..."
	deactivate || exit 0
	rm -rf ./.git/hooks
	rm -rf ./.venv/

run:
	uvicorn src.main:app --reload --port $(or $(PORT),8080)

format-code:
	poetry run pre-commit run --all-files
