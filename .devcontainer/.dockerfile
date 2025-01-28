FROM mcr.microsoft.com/vscode/devcontainers/python:3.12-bookworm

WORKDIR /work

RUN pip install pyproject.toml

EXPOSE 8000
