# Lab 6: Docker and GitActions

## Requirements
- Docker Desktop install - [download](https://www.docker.com/products/docker-desktop/) <br>
    Verify the installation by running a `hello-world` container
    ```
    docker run hello-world
    ```
- DockerHub Account - [SigUp](https://hub.docker.com/signup)

---

## Local Build and Testing

### Step 01: Download Source Code

* Dockerize a `FastAPI` application, Clone this branch `deploy-template`  <br>
* Setup a python virtual environment
    ```bash
    python3 -m venv demo
    source demo/bin/activate
    pip install -r requirements.txt
    ```

### Step 02: Initialize Dockerfile

A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.

* Create a file `Dockerfile` with contents

    ```Dockerfile
    FROM python:3.9-alpine

    RUN pip install --upgrade pip

    WORKDIR /app

    ADD . /app

    RUN pip install -r requirements.txt

    EXPOSE 8000

    CMD ["gunicorn" ,"-w", "4", "-k", "uvicorn.workers.UvicornWorker" , "--bind", "0.0.0.0:8000", "main:app"]
    ```

### Step 03: Build a docker image locally
Note: Keep your Docker Desktop running, verify its running by using `docker ps` 

* Before building the image verify the app

    ```bash
    uvicorn main:app --reload
    ```

    Open `localhost:8000` and should display,
    ```plaintext
    {"message":"Welcome, to this Docker Tutorial"}
    ```

* Stop the `uvicorn` server

* Lets, build an image now using `docker build` <br>
    The `docker build` command builds Docker images from a `Dockerfile` and a “context”

    ```bash
    cd /path/to/repo/dir

    docker build -t demofastapi:v1 .
    ```

* Verify the image creation using `docker images`

    ```bash
    docker images

    # Output
    REPOSITORY      TAG     IMAGE ID        CREATED             SIZE
    demofastapi     v1      83cdf13fa617    27 seconds ago      164MB
    ```

* Run the docker container using the image we build using `docker run`
    ```
    docker run -p 8080:8000 demofastapi:v1
    ```

* Open `localhost:8080` and should display, note we have mapped local port `8080` with container port `8000`
    ```plaintext
    {"message":"Welcome, to this Docker Tutorial"}
    ```

### Step 04: Push docker image to DockerHub Registry


* Tag the build image using `docker tag`
    > `docker tag <local_image_name>:<tag> <dockerhub_id>/<image_name>:<tag>`
    ```
    docker tag demofastapi:v1 anku22/demofastapi:latest
    ```

* Push the tagged image to DockerHub Registry using `docker push`

    > `docker push <dockerhub_id>/<image_name>:<tag>`

    ```
    docker push anku22/demofastapi:latest
    ```

* Verify the image is pushed to the Registry and run locally 
    ```
    docker run -p 8080:8000 anku22/demofastapi
    ```

---

## GitActions for Automated build and Push to Registry

### Step 01: Create Secrets from DockerHub and configure in GitHub Repo

* Have the following handy from DockerHub
    ```
    DOCKERHUB_USERNAME = anku22
    DOCKERHUB_TOKEN = <TOKEN>
    ```

* Configure the above in the Github Repo Settings

    Setting -> Security -> Secrets -> Actions  -> New repository secrets

### Step 02: Create workflow
* Create a file `dockerhub.yml` under `.github/workflows`

    ```yml
    name: ci

    on:
      push:
        branches:
          - 'deploy-template'      ## Update the branch name

    jobs:
      docker:
        runs-on: ubuntu-latest
        steps:
          -
            name: Set up QEMU
            uses: docker/setup-qemu-action@v2
          -
            name: Set up Docker Buildx
            uses: docker/setup-buildx-action@v2
          -
            name: Login to DockerHub
            uses: docker/login-action@v2
            with:
              username: ${{ secrets.DOCKERHUB_USERNAME }}
              password: ${{ secrets.DOCKERHUB_TOKEN }}
          -
            name: Build and push
            uses: docker/build-push-action@v3
            with:
              push: true
              tags: anku22/fastapi:latest # Update the dockerhub_id, image_name and tag
    ```

* Commit the changes.

* Verify the GitActions build process and Dockerhub


## Further reading

* Images from Dockerhub cannot be pulled into GCP Cloud Run / AWS
* Push images to cloud service provider registry and create a service
