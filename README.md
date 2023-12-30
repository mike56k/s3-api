## S3 Bucket Viewer API

Сервис монтирует в заданную папку внутри докер-образа бакет объектного хранилища S3 и предоставляет методы REST API для чтения этих файлов.

## Запуск контейнера

1. `git clone https://github.com/mike56k/s3-api.git`
1. `cd s3-api/docker`
1. `echo <идентификатор_ключа>:<секретный_ключ> > .passwd-s3fs` ([файл с креденшелами от Yandex Cloud](https://cloud.yandex.ru/ru/docs/storage/tools/s3fs))
1. `chmod 600 .passwd-s3fs`
1. `docker-compose up -d`
1.  Swagger для API будет доступен по адресу http://localhost:5000/

Также можно сконфигурировать директорию, в которую будет смонтирован S3-бакет, и название бакета в файле `docker/.env`
