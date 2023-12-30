#!/bin/bash

python3 -m flask run --host=0.0.0.0 &

s3fs mpi-2023 /mnt/s3 -o passwd_file=/root/.passwd-s3fs,nonempty,rw,allow_other,mp_umask=000 -o url=https://storage.yandexcloud.net,endpoint=eu-central-2,use_path_request_style -o dbglevel=info -f -o curldbg &

wait -n

exit $?