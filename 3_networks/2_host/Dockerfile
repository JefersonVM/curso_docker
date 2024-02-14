FROM python:3

RUN apt-get update -y && \
  apt-get install -y python3-pip python3-dev libpq-dev

WORKDIR /app

RUN pip install Flask requests psycopg2-binary

COPY . .

EXPOSE 5000

CMD ["python", "./app.py"]