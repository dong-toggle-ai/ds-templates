init:
	git init
	git branch -m main

install:
	python3 -m venv ./venv
	curl -sSL https://install.python-poetry.org | python3 -
	/venv/bin/poetry install
	pre-commit install

lint:
	flake8 .

test:
	pytest
