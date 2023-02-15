# ds-templates

## Setup
1) install cookiecutter
`pip install cookiecutter`

2) run the template:
`cookiecutter https://github.com/dong-toggle-ai/ds-templates.git`

## Makefile

- `make init` will run git init in current project
- `make install` will create virtual envs `venv` in current project, and also it'll install poetry and pre-commit
- `make lint` will run flake8
- `make test` will run pytest
- `make clean` will remove `venv`