#!/bin/bash

DOCKERFILE_PATH="./deployments/data/download_data/Dockerfile"
PROJECT_PATH="services/data/download_data"

# Set Docker environment to Minikube
eval $(minikube docker-env)

# Build a Docker image using variables for paths
docker build -t download-data-app:latest -f $DOCKERFILE_PATH $PROJECT_PATH
