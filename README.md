-   command to build docker image:

    -   `docker build -t python-fastapi .`

-   command to start the image as container:

    -   `docker run -p 80:80 python-fastapi`
    -   `docker run --name mycontainer -p 80:80 python-fastapi`

-   command to build the container with the image:

    -   `docker-compose -f docker-fastapi.yml build`
    -   `docker-compose -f docker-fastapi.yml build --no-cache` -- use this to build container without cache

-   command to start the container up:

    -   `docker-compose -f docker-fastapi.yml up`

-   practice problem:

    so your first task:
    Using FastAPI create a date-time API.
    /v1/now will return ISO8601 time of NOW in UTC.
    /v1/now?as_integer=1 will return as epoch timestamp.

    Then, create a docker image for this.
    As the end result, I expect this:
    docker run <image-tag> python app.py
    to start running the API.
