# step 1: initialise the docker image
FROM python:3.8-bullseye

# step 2: set the working directory inside docker
WORKDIR /src/app

# copy requirements.txt inside docker
COPY ./requirements.txt /src/app/requirements.txt

# install requirements.txt file
RUN pip install -r requirements.txt

# remove the requirements.txt from docker
CMD ["rm", "-rf", "/src/app/requirements.txt"]

# copy project directory content from local to docker 
COPY ./app /src/app

# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]