# Use the official Python image from Docker Hub as the base image
FROM python:3.10-slim

# Set the working directory to /app in the container
WORKDIR /app

# Copy all files from the current directory to /app in the container
COPY . .

# Install Python dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask (or your Python app) to communicate
EXPOSE 5000

# Define the default command to run your application
CMD ["python", "app.py"]
