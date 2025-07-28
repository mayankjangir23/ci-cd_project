Flask CI/CD App with Docker & Jenkins
-------------------------------------
This is a simple Flask application designed to demonstrate a basic **CI/CD pipeline** using Docker and Jenkins. The pipeline includes building the app, testing it, containerizing it, and optionally deploying it.

Project Structure
--------------------
├── app.py # Main Flask application
├── test_app.py # Simple test file
├── requirements.txt # Python dependencies
├── Dockerfile # Docker container definition
└── Jenkinsfile # CI/CD pipeline configuration

Requirements
-------------
- Python 3.8+ (for local testing)
- Docker installed and running
- Git
- Jenkins server (with Docker access)
- Docker Hub (or other container registry account)

Getting Started
----------------
1. Run the Flask app locally

2. Build & Run with Docker
   . docker build -t flask-ci-cd-app .
   . docker run -d -p 5000:5000 flask-ci-cd-app

Running Tests
-------------
python -m unittest test_app.py

Jenkins Pipeline Flow:
---------------------
Clone repo from GitHub
Install dependencies
Run tests
Build Docker image
Push Docker image to Docker Hub
Optionally deploy the app
