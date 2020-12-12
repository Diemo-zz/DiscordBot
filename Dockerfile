FROM ubuntu:20.04
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt install python3 python3-pip -y

WORKDIR "/"
COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

ARG DISCORD_BOT_TOKEN
ENV DISCORD_BOT_TOKEN=$DISCORD_BOT_TOKEN

COPY app /app

COPY app.py /app.py

ENTRYPOINT ["python3", "app.py"]


