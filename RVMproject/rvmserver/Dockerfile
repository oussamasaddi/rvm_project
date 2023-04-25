# Use an official Python runtime as a parent image
FROM python:3.9



RUN apt-get update -y && \
    apt-get install build-essential cmake pkg-config -y

RUN pip install dlib==19.9.0

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the application requirements
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point of the container to the application
ENTRYPOINT ["python", "app.py"]
