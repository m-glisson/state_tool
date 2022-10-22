# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster
#ENV FLASK_RUN_PORT=8000
WORKDIR /state-tool

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]