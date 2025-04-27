FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /app/media/books/covers
RUN chmod -R 755 /app/media

RUN chmod +x /app/start.sh

EXPOSE 8000

CMD ["./start.sh"]