# Makefile for Django News Aggregator project

PYTHON := python
PIP := pip
MANAGE := $(PYTHON) manage.py

.PHONY: help install lint format test pre-commit-run check run

help:
	@echo "Available commands:"
	@echo "  make install         Install dependencies from requirements.txt"
	@echo "  make lint            Run ruff to check for linting issues"
	@echo "  make format          Run black to auto-format code"
	@echo "  make test            Run pytest"
	@echo "  make pre-commit-run  Run all pre-commit hooks on all files"
	@echo "  make check           Run lint, format check, and tests"
	@echo "  make run             Run Django development server"

install:
	@echo "📦 Installing dependencies..."
	pip install -r requirements.txt

lint:
	@echo "🔍 Linting with ruff..."
	ruff check .

format:
	@echo "🎨 Formatting with black..."
	black .

test:
	@echo "🧪 Running tests with pytest..."
	pytest

check: lint test
	@echo "✅ All checks passed."

runserver:
	@echo "🚀 Starting Django development server..."
	$(MANAGE) runserver

dev: format lint test runserver
