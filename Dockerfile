FROM python:3.11.0

WORKDIR /app

COPY . .

ENTRYPOINT ["python3", "src/main.py"]
