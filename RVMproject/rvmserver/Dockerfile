# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        cmake \
        build-essential \
        libopenblas-dev \
        liblapack-dev \
        libjpeg-dev \
        libpng-dev \
        libtiff-dev \
        libavcodec-dev \
        libavformat-dev \
        libswscale-dev \
        libv4l-dev \
        libxvidcore-dev \
        libx264-dev \
        libgtk-3-dev \
        libatlas-base-dev \
        gfortran \
        wget \
        unzip \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir numpy

# Download and build dlib
RUN mkdir -p /opt/dlib && \
    cd /opt/dlib && \
    wget http://dlib.net/files/dlib-19.22.tar.bz2 && \
    tar xvf dlib-19.22.tar.bz2 && \
    cd dlib-19.22 && \
    python setup.py install --yes USE_AVX_INSTRUCTIONS --no DLIB_USE_CUDA && \
    cd .. && \
    rm -rf dlib-19.22*

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the application requirements
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point of the container to the application
ENTRYPOINT ["python", "app.py"]
