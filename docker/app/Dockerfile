FROM python:latest

WORKDIR /home

COPY . .

RUN apt-get update && apt-get install -y wait-for-it
RUN python3 -m venv venv && . venv/bin/activate
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
