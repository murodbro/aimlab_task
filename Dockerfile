FROM python:3.13.3-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /app/media/books/covers
RUN chmod -R 755 /app/media

RUN chmod +x /app/start.sh

EXPOSE 8000

CMD ["./start.sh"]