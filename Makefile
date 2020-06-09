.PHONY: install install-dev lint format test

all: format lint coverage

install:
	pip install -e .

install-dev:
	pip install -e .[dev]

lint:
	flake8 --count --show-source --statistics

format:
	black --check .

test:
	pytest tests/

coverage:
	pytest --cov=django_gvar/ tests/
