FROM python:3.11-buster as requirements

RUN pip install poetry==2.0.1 poetry-plugin-export==1.9.0

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /work

COPY pyproject.toml poetry.lock ./

RUN poetry export --format=requirements.txt > requirements.txt

FROM mcr.microsoft.com/vscode/devcontainers/python:3.12-bookworm

COPY --from=requirements /work/requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt  

EXPOSE 8000
