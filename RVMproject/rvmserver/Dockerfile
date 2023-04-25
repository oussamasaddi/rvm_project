# Use an official Python runtime as a parent image
FROM python:3.9



RUN apt-get update -y && \
    apt-get install build-essential cmake pkg-config -y

RUN pip install dlib==19.24.1


# Install the application requirements
RUN pip install --no-cache-dir -r rvmserver\requirements.txt

RUN python rvmserver\manage.py runserver
