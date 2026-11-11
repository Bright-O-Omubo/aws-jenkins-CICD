# aws-jenkins-CICD

# Simple Flask Web App

A small Flask application with a homepage and a health-check endpoint.

## Run locally

Requires Python 3.10+.

```bash
python -m venv .venv
```

Activate the environment:

- Linux/macOS: `source .venv/bin/activate`
- Windows PowerShell: `.venv\\Scripts\\Activate.ps1`

Install dependencies and start the app:

```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:8081` in your browser. Check `http://127.0.0.1:8081/health`
for a JSON health response.

## Run with Docker

Build the image:

```bash
docker build -t <imageName>:<imageTag> .
```

Start a container and map host port 8081 to container port 5000

```bash
docker run --name <containerName> -p 8081:5000 <imageName>
```
To Access the web page 
Open `http://localhost:8081`

To stop and remove the container:

```bash
docker stop flask-demo
docker rm flask-demo
```

## Important notes

- `EXPOSE 5000` documents the container port; it does not publish the port by itself.
- `-p 8080:5000` maps host port 8081 to container port 5000.

