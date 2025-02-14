# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app directory into the container
COPY . .

# Expose the port the app will run on
EXPOSE 8080

# Define environment variable for Flask to bind to all network interfaces
ENV FLASK_RUN_HOST=0.0.0.0

# Run application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app:app"]