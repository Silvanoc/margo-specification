FROM mcr.microsoft.com/vscode/devcontainers/python:3.12-bookworm

RUN pip install mkdocs \
    && pip install mkdocs-markdownextradata-plugin \
    && pip install mkdocs-material \
    && pip install poetry \
    && pip install linkml 

EXPOSE 8000