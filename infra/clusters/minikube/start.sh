#!/bin/bash

# restart Minikube
minikube start

# switch kubectl to Minikube context
kubectl config use-context minikube
