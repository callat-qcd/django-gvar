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


VERSION:=$(shell python setup.py --version)

version:
	@echo $(VERSION)

create-dist: all
	python -m pip install --upgrade setuptools wheel twine
	python setup.py sdist bdist_wheel

pypi-test-upload: create-dist
	@echo "---------------------------------------------------------"
	@echo "Start uploading djang-gvar version ${VERSION} to testpypi"
	@echo "---------------------------------------------------------"
	python -m twine upload --repository testpypi dist/django_gvar-${VERSION}*

pypi-main-upload: pypi-test-upload
	@echo"---------------------------------------------------------"
	@echo "Start uploading djang-gvar version ${VERSION} to mainpypi"
	@echo"---------------------------------------------------------"
	python -m twine upload dist/django_gvar-${VERSION}*
