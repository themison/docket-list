# base image
FROM python:3

#directory to store app source code
RUN mkdir /code

#switch to /app directory so that everything runs from here
WORKDIR /code

#copy the app code to image working directory
COPY . /code

#let pip install required packages
RUN pip install -r requirements.txt