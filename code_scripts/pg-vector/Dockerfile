FROM python:3.12-alpine

RUN sudo apt update \ 
    pip3 install psycopg2-binary numpy

WORKDIR /app

COPY db_with_embedding.py /app

CMD [ "python3", "/app/db_with_embedding.py"]