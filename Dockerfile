FROM tiangolo/uwsgi-nginx-flask:latest

ENV LISTEN_PORT 8080
EXPOSE 8080

COPY ./app /app
RUN pip install flask_uploads