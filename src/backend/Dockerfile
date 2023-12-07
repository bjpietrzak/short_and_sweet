FROM python:3.11-slim-buster

WORKDIR /app

COPY ./backend/requirements.txt .

RUN pip install -r requirements.txt

COPY ./backend/ .