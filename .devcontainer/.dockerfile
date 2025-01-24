FROM mcr.microsoft.com/vscode/devcontainers/python:3.12-bookworm

RUN pip install poetry  

EXPOSE 8000