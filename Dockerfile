# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the Python script into the container
COPY . /app

# Install necessary Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Expose the port the app runs on
EXPOSE 9100

# Run the Python application
CMD ["python", "main.py"]
