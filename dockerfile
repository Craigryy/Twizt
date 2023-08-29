# Specify the base image
FROM python:3.10-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files
COPY . .

# Copy requirements.txt
COPY requirements.txt .

# Create a non-root user
RUN adduser --disabled-password --gecos '' myuser

# Switch to the non-root user
USER myuser

# Install the Python dependencies
RUN pip install -r requirements.txt

# Expose the ports on which the Flask app will run
EXPOSE 5000

# Set the command to run the Flask app
CMD ["python", "app.py"]
