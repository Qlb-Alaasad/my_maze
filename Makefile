# A-Maze-ing Makefile
# 42 Curriculum Project
# Made by: mabu-are, aabtah

PYTHON := python3
PIP := $(PYTHON) -m pip
VENV := .venv
VENV_PYTHON := $(VENV)/bin/python
VENV_PIP := $(VENV)/bin/pip

# Main script
SCRIPT := a_maze_ing.py
CONFIG := config.txt

# Default target
.PHONY: all
all: install

# Install dependencies (auto-creates and activates venv if not exists)
.PHONY: install
install:
	@if [ ! -d "$(VENV)" ]; then 		echo "Creating virtual environment..."; 		$(PYTHON) -m venv $(VENV); 	fi
	@echo "Installing dependencies in virtual environment..."
	$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install flake8 mypy pytest
	$(VENV_PIP) install pydantic
	@echo ""
	@echo "========================================"
	@echo "Dependencies installed successfully!"
	@echo "To activate the virtual environment, run:"
	@echo "  source $(VENV)/bin/activate"
	@echo "========================================"

# Run the main script (auto-uses venv if exists)
.PHONY: run
run:
	@if [ -d "$(VENV)" ]; then 		$(VENV_PYTHON) $(SCRIPT) $(CONFIG); 	else 		$(PYTHON) $(SCRIPT) $(CONFIG); 	fi

# Run in debug mode with pdb (auto-uses venv if exists)
.PHONY: debug
debug:
	@if [ -d "$(VENV)" ]; then 		$(VENV_PYTHON) -m pdb $(SCRIPT) $(CONFIG); 	else 		$(PYTHON) -m pdb $(SCRIPT) $(CONFIG); 	fi

# Clean temporary files and caches
.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .venv
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

# Run linting with flake8 and mypy (auto-uses venv if exists, excludes .venv)
.PHONY: lint
lint:
	@if [ -d "$(VENV)" ]; then 		$(VENV_PIP) install flake8 mypy; 		$(VENV_PYTHON) -m flake8 . --exclude=$(VENV); 		$(VENV_PYTHON) -m mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs --exclude=$(VENV); 	else 		flake8 . --exclude=$(VENV); 		mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs --exclude=$(VENV); 	fi

# Run strict linting (auto-uses venv if exists, excludes .venv)
.PHONY: lint-strict
lint-strict:
	@if [ -d "$(VENV)" ]; then 		$(VENV_PYTHON) -m flake8 . --exclude=$(VENV); 		$(VENV_PYTHON) -m mypy . --strict --exclude=$(VENV); 	else 		flake8 . --exclude=$(VENV); 		mypy . --strict --exclude=$(VENV); 	fi

# Run tests (auto-uses venv if exists)
.PHONY: test
test:
	@if [ -d "$(VENV)" ]; then 		$(VENV_PYTHON) -m pytest -v; 	else 		pytest -v; 	fi

# Build the reusable package (requires pyproject.toml or setup.py)
.PHONY: build
build:
	@if [ -d "$(VENV)" ]; then 		$(VENV_PIP) install build; 	fi
	@echo "Building package..."
	@if [ -f pyproject.toml ] || [ -f setup.py ]; then 		if [ -d "$(VENV)" ]; then 			$(VENV_PYTHON) -m build; 		else 			$(PYTHON) -m build; 		fi 	else 		echo "Warning: pyproject.toml or setup.py not found. Skipping package build."; 		echo "Create pyproject.toml to build the mazegen package."; 	fi

# Create virtual environment only
.PHONY: venv
venv:
	@if [ ! -d "$(VENV)" ]; then 		echo "Creating virtual environment..."; 		$(PYTHON) -m venv $(VENV); 		echo "Virtual environment created at $(VENV)"; 		echo "Run 'source $(VENV)/bin/activate' to activate it."; 	else 		echo "Virtual environment already exists at $(VENV)"; 	fi

# Run in virtual environment
.PHONY: venv-run
venv-run: venv
	$(VENV_PYTHON) $(SCRIPT) $(CONFIG)

# Help
.PHONY: help
help:
	@echo "A-Maze-ing - Made by mabu-are, aabtah"
	@echo ""
	@echo "Available targets:"
	@echo "  install      - Create venv + install all dependencies (flake8, mypy, pytest, pydantic)"
	@echo "  run          - Execute the main script (uses venv if exists)"
	@echo "  debug        - Run with Python debugger (uses venv if exists)"
	@echo "  clean        - Remove temporary files, caches, and venv"
	@echo "  lint         - Run flake8 and mypy (uses venv if exists, excludes .venv)"
	@echo "  lint-strict  - Run strict linting (uses venv if exists, excludes .venv)"
	@echo "  test         - Run pytest (uses venv if exists)"
	@echo "  build        - Build the reusable package (needs pyproject.toml)"
	@echo "  venv         - Create virtual environment only"
	@echo "  venv-run     - Run in virtual environment"
	@echo "  help         - Show this help message"
