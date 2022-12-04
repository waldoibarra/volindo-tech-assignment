FROM python:3.11.0

WORKDIR /app

COPY . .

CMD ["python3", "src/main.py"]
