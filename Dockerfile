# Use the latest Ubuntu as the base image
FROM ubuntu:latest

# Set a label for the author
LABEL authors="rafae"

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the contents of the current directory into the container's /app directory
COPY . /app

# Update package lists and install Python 3 and pip3
RUN apt-get update && apt-get install -y python3 python3-pip

# Upgrade pip to the latest version
RUN pip3 install --upgrade pip

# Install Python dependencies from the requirements.txt file
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Install nmap, a network scanning tool
RUN apt-get install -y nmap

# Install Flask, python-nmap, and psutil Python libraries
RUN pip3 install flask python-nmap psutil

# Expose port 80 for the web application
EXPOSE 80

# Define the command to run when the container starts, which is running app.py
CMD ["python3", "app.py"]
