FROM python:3.6.3
ARG WEB_SERVER_PORT=8080
ENV WEB_SERVER_PORT=$WEB_SERVER_PORT
ARG HOST=0.0.0.0
ENV HOST=$HOST
EXPOSE $WEB_SERVER_PORT
RUN pip install pipenv
WORKDIR /src/
ADD . /src/
RUN pipenv install --system --deploy
RUN apistar create_tables
ENTRYPOINT apistar run --no-debug --no-reloader --host=$HOST --port=$WEB_SERVER_PORT