FROM python:3.11-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /app .

EXPOSE 8080

CMD ["python", "main.py"]