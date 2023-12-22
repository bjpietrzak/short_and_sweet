FROM python:3.11-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get -y install gcc

RUN pip install --upgrade pip && \
    pip install -r requirements.txt
