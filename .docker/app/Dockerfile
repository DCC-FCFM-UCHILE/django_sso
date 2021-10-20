FROM python:3.10.0-slim-bullseye
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y dist-upgrade \
    && apt-get -y install libpq-dev gcc cron

RUN pip install --upgrade pip
COPY app/ .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt
