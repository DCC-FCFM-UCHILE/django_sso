FROM python:3.8.13-slim-bullseye
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y dist-upgrade \
    && apt-get -y install libpq-dev gcc build-essential zip --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY app/ .

RUN pip install --upgrade pip \
    && pip install -r _requirements/base.txt -r _requirements/production.txt
