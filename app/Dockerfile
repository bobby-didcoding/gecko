############ BUILDER ############

### 1. Pull offical Python
FROM python:3.10-slim as builder

### 2. Create working directory
WORKDIR /usr/src/app

### 3. Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

### 4. Build wheels and requirements
RUN pip install --upgrade pip
RUN pip install pip-tools
COPY . /usr/src/app/
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

########## FINAL ##########

### 1. Pull offical Python
FROM python:3.10-slim

### 2. Add Environment variables
ENV DOCKERIZE_VERSION v0.6.1

### 3. Create working directory
RUN mkdir /app
WORKDIR /app

### 4. Install dependancies
RUN apt-get update && apt-get -y install wget;

### 5. Add dockerize to allow waiting for the DB to load.
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \ 
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \ 
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

### 6. Install dependancies
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

### 7. Copy project to container
COPY . /app/
