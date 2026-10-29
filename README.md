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

Open `http://127.0.0.1:5000` in your browser. Check `http://127.0.0.1:5000/health`
for a JSON health response.

## Run with Docker

Build the image:

```bash
docker build -t simple-flask-app .
```

Start a container and map host port 8080 to container port 5000:

```bash
docker run --name flask-demo -p 8080:5000 simple-flask-app
```

Open `http://localhost:8080`.

To stop and remove the container:

```bash
docker stop flask-demo
docker rm flask-demo
```

## Important notes

- `EXPOSE 5000` documents the container port; it does not publish the port by itself.
- `-p 8080:5000` maps host port 8080 to container port 5000.
- This built-in Flask server is for development and learning, not production deployment.
- For a production-style setup, run a WSGI server such as Gunicorn and optionally put Nginx in front as a reverse proxy.

