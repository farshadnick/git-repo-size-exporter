FROM python:3.11-alpine

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .

# Expose the port (make sure this matches your app)
EXPOSE 9400

# Set the environment variable for Flask
ENV FLASK_APP=main.py

# Run the application
CMD ["python", "main.py"]
