# Homework

This folder contains the homework assignment for the ML Zoomcamp deployment module.

## Contents

- `predict.py` - FastAPI application for lead scoring predictions
- `test.py` - Test script to send requests to the prediction API
- `pipeline_v1.bin` - Pre-trained machine learning model
- `Dockerfile` - Docker configuration for containerizing the application

## Usage

### Build the Docker image

```bash
cd /workspaces/ML-zoomcamp/05-deployment
docker build -f homework/Dockerfile -t homework-predict .
```

### Run the container

```bash
docker run -it --rm -p 9696:9696 homework-predict
```

### Test the API

In another terminal:

```bash
cd /workspaces/ML-zoomcamp/05-deployment/homework
uv run python test.py
```
