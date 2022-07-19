FROM python:3.9-alpine

RUN pip install --upgrade pip

WORKDIR /app

COPY main.py            \
     requirements.txt   \
     ./

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn" ,"-w", "4", "-k", "uvicorn.workers.UvicornWorker" , "--bind", "0.0.0.0:8000", "main:app"]