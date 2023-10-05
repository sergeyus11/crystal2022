FROM python:3.11.2

EXPOSE 8000

RUN apt-get update && apt-get install -y python3-dev vim less libxml2-dev libxslt1-dev

WORKDIR /opt/crystal
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

WORKDIR /opt/crystal/app/
COPY ./app.ini /opt/finproject/app.ini
COPY ./docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]
