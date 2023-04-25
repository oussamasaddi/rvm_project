FROM python:3.9

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    libgtk-3-dev \
    libboost-all-dev \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel

# Clone the dlib repository and build it
RUN apt-get update -y && \
    apt-get install build-essential cmake pkg-config -y

RUN pip install dlib==19.9.0

# Create a new user and group to run the application
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# Set the working directory
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY . /app

# Set the ownership of the application files
RUN chown -R appuser:appgroup /app

# Switch to the appuser
USER appuser

# Start the Django application
CMD python manage.py runserver 0.0.0.0:$PORT
