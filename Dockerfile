FROM python:3.11-slim

# set working directory
WORKDIR /code

# install system deps
RUN apt-get update && apt-get install -y libpq-dev gcc

# install python deps
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . /code/
