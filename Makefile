PYTHON_BINARY := python3
PROJECT_NAME := ersilia-precalc-poc
TEST_DIR := tests
VIRTUAL_ENV := .venv
VIRTUAL_BIN := $(VIRTUAL_ENV)/bin
.PHONY: help install clean black lint format test

## help - Display help about make targets for this Makefile
help:
	@cat Makefile | grep '^## ' --color=never | cut -c4- | sed -e "`printf 's/ - /\t- /;'`" | column -s "`printf '\t'`" -t

## install - Install virtual environment
install:
	@echo "Installing..."
	@if [ "$(shell which poetry)" = "" ]; then \
		$(MAKE) install-poetry; \
	fi
	@$(MAKE) setup-poetry

install-poetry:
	@echo "Installing poetry..."
	@curl -sSL https://install.python-poetry.org | python3 -
	@export PATH="$HOME/.local/bin:$PATH"

setup-poetry:
	@poetry env use python3 && poetry install

## clean - Remove the virtual environment and clear out .pyc files
clean:
	rm -rf $(VIRTUAL_ENV) dist *.egg-info .coverage
	find . -name '*.pyc' -delete

## black - Runs the Black Python formatter against the project
black:
	$(VIRTUAL_BIN)/black $(PROJECT_NAME)/ $(TEST_DIR)/

## format - Runs all formatting tools against the project
format: black lint

## lint - Lint the project
lint:
	$(VIRTUAL_BIN)/ruff $(PROJECT_NAME)/ $(TEST_DIR)/

## mypy - Run mypy type checking on the project
mypy:
	$(VIRTUAL_BIN)/mypy $(PROJECT_NAME)/ $(TEST_DIR)/

## test - Test the project
test:
	$(VIRTUAL_BIN)/pytest