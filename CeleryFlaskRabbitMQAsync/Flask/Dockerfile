# Specify the base image
FROM python:3.9-slim-buster

# Upgrade pip
RUN pip install --upgrade pip

# Copy the requirements file to the Docker container
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

RUN pip install celery[amqp]

RUN pip install --upgrade Flask werkzeug gunicorn celery pika

# Set the working directory
WORKDIR /app

# Copy the application code to the Docker container
COPY . .

# Start the application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
