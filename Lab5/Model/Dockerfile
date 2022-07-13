# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY requirements.txt /code/requirements.txt

# 
# COPY tensorflow-2.4.1-py3-none-any.whl /code/tensorflow-2.4.1-py3-none-any.whl

# 
RUN pip3 install tensorflow tensorflow-gpu

# 
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
