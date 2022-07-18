FROM python:3.6

COPY . /src

COPY ./requirements.txt /src/requirements.txt

WORKDIR src


RUN pip install -r requirements.txt

CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--reload" ]