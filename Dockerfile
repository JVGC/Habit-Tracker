FROM python:3.10.11-alpine3.18

ENV PYTHONUNBUFFERED 1

COPY ./pyproject.toml /
COPY ./README.md /

COPY ./backend /backend
WORKDIR /backend

EXPOSE 8000


RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install


