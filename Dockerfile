FROM python:3.12-slim as base

ARG POETRY_VERSION=1.5.1

ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN apt update -y && apt install -y gcc
RUN python -m pip install --upgrade pip
RUN python -m pip install --upgrade setuptools wheel poetry==${POETRY_VERSION}
RUN apt-get update && apt-get install systemd gettext -y

COPY poetry.lock ./
COPY pyproject.toml ./

RUN poetry config installer.max-workers 10 && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . .

RUN chmod +x ./scripts/startup.sh
CMD ./scripts/startup.sh