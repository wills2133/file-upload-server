FROM tiangolo/uwsgi-nginx-flask:latest

COPY ./app /app
RUN pip install flask_uploads