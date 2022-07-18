#!/bin/bash

FROM python:3.9

COPY . /app

WORKDIR app

RUN pip install -r requirements.txt

EXPOSE 8001

CMD ["gunicorn" ,"-w", "4", "-k", "uvicorn.workers.UvicornWorker" , "--bind", "0.0.0.0:8001", "main:app"]
