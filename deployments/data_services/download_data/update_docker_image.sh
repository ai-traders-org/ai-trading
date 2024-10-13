#!/bin/bash

DOCKERFILE_PATH="./deployments/data_services/download_data/Dockerfile"
PROJECT_PATH="services/data_services/download_data"

# Set Docker environment to Minikube
eval $(minikube docker-env)

# Build a Docker image using variables for paths
docker build -t download-data-app:latest -f $DOCKERFILE_PATH $PROJECT_PATH
