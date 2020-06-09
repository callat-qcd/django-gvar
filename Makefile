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

VERSIONFILE:=django_gvar/_version.py
VERSION:=$(shell cat $(VERSIONFILE))

create-dist: all
	python -m pip install --upgrade setuptools wheel twine
	python setup.py sdist bdist_wheel

pypi-test-upload: create-dist
	@echo "Start uploading djang-gvar version ${VERSION} to testpypi"
	# python -m upload --repositiory testpypi dist/django_gvar-${VERSION}*
