# PY-scan-network
# Software Detection and Dockerized Web Interface

This project aims to create a Python application that checks if a specific software is running on computers in the local network and provides a Dockerized web interface to visualize the results.

## Prerequisites

Before you start the project, ensure you have the following dependencies installed:

- Python 3
- Docker
- pip3 (Python package manager)

You can install the necessary Python libraries using the following command:

```bash
pip3 install flask python-nmap psutil
```

to run the project ensure that you are at the root and run the followin command 

python generate_yml.py ; docker-compose up --build

After that to visualize the results go to

localhost:5000/process
