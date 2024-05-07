FROM python:3.9-slim-buster

ENV DOCKER_CONTAINER=true

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

COPY src/ /src/
RUN pip install -e /src
COPY tests/ /tests/
