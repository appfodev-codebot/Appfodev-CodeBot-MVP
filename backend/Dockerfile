# Use an official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the code to the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask application
CMD ["python", "main.py"]
