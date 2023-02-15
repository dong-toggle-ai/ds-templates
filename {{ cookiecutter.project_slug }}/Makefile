VENV = venv

init:
	@echo "Initialize git..."
	git init
	git branch -m main

install:
	@echo "Creating virtualenv venv..."
	python3 -m venv ${VENV}

	@echo "Downloading poetry and install packages..."
	curl -sSL https://install.python-poetry.org | python3 -
	${HOME}/.local/bin/poetry install


	@echo "Setup pre-commit..."
	pre-commit install

lint:
	@echo "Running flake8..."
	flake8 .

test:
	@echo "Running pytest..."
	pytest

clean:
	@echo "Cleaning up..."
	rm -rf ${VENV}
