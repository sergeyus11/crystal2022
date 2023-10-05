FROM nginx:1.13

EXPOSE 80 443

RUN apt-get update && apt-get -y install logrotate

COPY ./app.conf /etc/nginx/sites-enabled/
COPY ./nginx.conf /etc/nginx/

COPY ./logrotate.conf /etc/logrotate.d/nginx
RUN chmod 0644 /etc/logrotate.d/nginx

CMD service cron start && nginx -g 'daemon off;'
