# Use an official Python runtime as a parent image
FROM python:3.11-slim


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
# Set the PYTHONPATH environment variable
ENV PYTHONPATH /app
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV PYTHONPATH /app

# Run app.py when the container launches
CMD ["python", "guru/src/app.py"]
