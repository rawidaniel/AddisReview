FROM python:3.11.0

RUN addgroup app && adduser -S -G app app
RUN mkdir web_static
USER app
WORKDIR ./web_static

COPY . ./
EXPOSE 5000:80

CMD [ "python3 -m", "gunicorn --bind 0.0.0.0:5000 main:app" ]
