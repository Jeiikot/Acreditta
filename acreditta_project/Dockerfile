FROM python:latest

ENV PYTHONUNBUFFERED 1

WORKDIR /acreditta
COPY requirements.txt /acreditta/
RUN pip install -r requirements.txt
COPY . /acreditta/
EXPOSE 8000
