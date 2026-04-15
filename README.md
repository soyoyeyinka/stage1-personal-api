
# Stage 1 Personal API

This is a simple Flask API built for the HNG DevOps Stage 1 task.

## Project Description

This API provides three endpoints that return JSON responses for service status, health check, and personal details.

## Tech Stack

- Python
- Flask
- Gunicorn
- Nginx
- Ubuntu VPS

## Local Setup

Clone the repository:

git clone https://github.com/soyoyeyinka/stage1-personal-api.git
cd stage1-personal-api

## Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

##Install dependencies:
Bash
pip install -r requirements.txt

##Run the app locally:
Bash
python app.py

##Endpoints
GET /
Response:

JSON
{
  "message": "API is running"
}

GET /health

Response:
JSON
{
  "message": "healthy"
}

GET /me

Response:
JSON
{
  "name": "Soyoye Olayinka",
  "email": "soyoyeolayinka35@gmail.com",
  "github": "https://github.com/soyoyeyinka"
}

##Live URL

Plain text
http://13.40.243.177

##Deployment
The application runs on an internal port using Gunicorn and is served publicly through Nginx reverse proxy. The service is managed with systemd to ensure it stays running persistently.




