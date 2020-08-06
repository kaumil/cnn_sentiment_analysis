FROM tiangolo/uwsgi-nginx-flask:latest
RUN apt-get update
ENV STATIC_URL /static
ENV STATIC_PATH app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install tensorflow
RUN pip install -r /var/www/requirements.txt