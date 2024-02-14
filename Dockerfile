# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Create a non-root user
RUN useradd -m myuser

# Set the working directory in the container to /app
WORKDIR /app

# Copy only necessary files into the container at /app
COPY bot_controller /app/bot_controller
COPY __main__.py /app/
COPY requirements.txt /app/
COPY .env /app/

# Load environment variables from .env file
RUN export $(cat .env | xargs)

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Switch to the non-root user
USER myuser

# Run __main__.py when the container launches
CMD ["python", "__main__.py"]