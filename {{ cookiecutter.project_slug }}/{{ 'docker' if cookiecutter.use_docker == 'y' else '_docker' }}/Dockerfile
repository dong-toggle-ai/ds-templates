ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}
LABEL maintainer="Toggle <deploy@toggle.ai>"

ENV SERVICE_NAME {{ cookiecutter.project_name }}
ENV PYTHONUNBUFFERED 1

# CREATE UNPRIVILEGED USER AND SET PERMISSIONS
RUN groupadd -g 10001 appuser && \
    useradd  -m -u 10001 -s /bin/bash -g appuser appuser

RUN mkdir -p /src/app; exit 0
COPY --chown=appuser:appuser . /src/app/
WORKDIR /src/app

USER appuser
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false && poetry install

# LIGHT IT UP
CMD ["python", ""]