FROM python:3.11-slim

WORKDIR /enceladus

COPY . /enceladus/

EXPOSE 8000

RUN pip install --upgrade pip && pip install gunicorn && pip install psycopg2-binary
RUN pip install --no-cache-dir -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000