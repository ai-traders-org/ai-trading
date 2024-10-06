#!/bin/bash

# stop cluster
minikube stop

# delete cluster
minikube delete --all --purge

# delete Minikube configuration files and data
rm -rf ~/.minikube

# delete docker images from Minikube
minikube ssh
docker system prune --all --volumes -f

# restart Minikube
minikube start

# switch kubectl to Minikube context
kubectl config use-context minikube