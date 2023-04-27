# Use an official Python runtime as a parent image
FROM python:3.9



RUN apt-get update -y && \
    apt-get install build-essential cmake pkg-config -y &&  apt-get install libgl1-mesa-glx

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install dlib==19.9.0


COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt
COPY . /opt/app

RUN python manage.py runserver
