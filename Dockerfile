FROM python:3.10-alpine

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

WORKDIR /app

COPY . /app

EXPOSE 8000

CMD python manage.py runserver