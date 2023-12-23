FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get -y install gcc

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# COPY ./app .

# EXPOSE 7070

# CMD ["uvicorn", "model_router:app", "--host", "0.0.0.0", "--port", "7070"]
