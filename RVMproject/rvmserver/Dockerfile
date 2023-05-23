# Use an official Python runtime as a parent image
FROM python:3.9



RUN apt-get update -y && \
    apt-get install build-essential cmake pkg-config -y 


RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install dlib==19.9.0


COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

CMD [ "python3" ,"manage.py", "runserver","0.0.0.0:8000" ]
