FROM ubuntu:20.04

RUN apt update && apt install -y s3fs && apt install -y python3-pip

RUN pip install flask

RUN mkdir /mnt/s3

COPY ../src/.passwd-s3fs /root/.passwd-s3fs
RUN chmod 600 /root/.passwd-s3fs

COPY ./src /app
WORKDIR /app

EXPOSE 8000

COPY ../docker/entrypoint.sh .
RUN chmod +x entrypoint.sh

CMD ["/bin/bash","-c","./entrypoint.sh"]