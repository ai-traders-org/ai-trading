#!/bin/bash

# Ustaw środowisko Dockera na Minikube
eval $(minikube docker-env)

# Przypisanie ścieżek do zmiennych
DOCKERFILE_PATH="../../../services/data/download_data/Dockerfile"
PROJECT_PATH="../../../services/data/download_data"

# Zbuduj obraz Dockerowy, używając zmiennych dla ścieżek
docker build -t download-data-app:latest -f $DOCKERFILE_PATH $PROJECT_PATH
