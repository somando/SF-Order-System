FROM python:latest

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y wait-for-it postgresql-client
RUN python3 -m venv venv && . venv/bin/activate
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
