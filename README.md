# AI_MODEL_TESTING (Flask + Docker + GitHub Actions → AWS EC2)

This repo is a ready-to-deploy CI/CD scaffold. Push to `main` and GitHub Actions will build a Docker image and deploy it to your EC2 via SSH.

## Endpoints
- `GET /` → Hello
- `GET /health` → `{ "status": "ok" }`

## Quick start
1) Create a **public** Docker Hub repo: `<DOCKERHUB_USERNAME>/ai_model_testing`
2) Set GitHub **Actions secrets** (see below)
3) Launch Ubuntu EC2 (t3.micro), open inbound **80** and **22**
4) Push to `main` → deployed automatically

### Required GitHub Secrets
- `DOCKER_USERNAME`
- `DOCKER_TOKEN`
- `IMAGE_NAME` → e.g. `docker.io/<DOCKERHUB_USERNAME>/ai_model_testing:latest`
- `EC2_HOST` → your EC2 public IP/DNS
- `EC2_USER` → `ubuntu`
- `EC2_SSH_KEY` → the **private key** content of your `.pem`

## Local run (optional)
```bash
cd app
pip install -r requirements.txt
gunicorn -b 0.0.0.0:8000 wsgi:app
```
Then browse http://localhost:8000
