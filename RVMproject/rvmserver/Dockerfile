# Use an official Python runtime as a parent image
FROM python:3.9



RUN apt-get update -y && \
    apt-get install build-essential cmake pkg-config -y

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install dlib==19.9.0


# Install the application requirements
RUN pip install -r requirements.txt

RUN python rvmserver\manage.py runserver
