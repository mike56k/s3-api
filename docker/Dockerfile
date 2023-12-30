FROM ubuntu:20.04

RUN apt update && apt install -y s3fs && apt install -y python3-pip

ARG S3_BUCKET_DIR
ARG BUCKET_NAME
ENV S3_BUCKET_DIR=$S3_BUCKET_DIR
ENV BUCKET_NAME=$BUCKET_NAME

COPY ../docker/requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir ${S3_BUCKET_DIR}

COPY ../docker/.passwd-s3fs /root/.passwd-s3fs
RUN chmod 600 /root/.passwd-s3fs

COPY ./src /app
WORKDIR /app

EXPOSE 8000

COPY ../docker/entrypoint.sh .
RUN chmod +x entrypoint.sh

CMD ["/bin/bash","-c","./entrypoint.sh"]