# Build stage
FROM python:3.11.0 AS build-stage
RUN mkdir web_static
WORKDIR ./web_static
COPY requerments.txt ./
RUN pip3 install -r requirements.txt
COPY . .
RUN python3 -m gunicorn --bind 0.0.0.0:5000 main:app


# Production stage
FROM nginx:1.12-alpine
RUN addgroup app && adduser -S -G app app
USER app
COPY --from=build-stage /web_static/build /usr/share/nginx/html
EXPOSE 80
ENTRYPOINT [ "nginx", "-g", "daemon off;" ]
