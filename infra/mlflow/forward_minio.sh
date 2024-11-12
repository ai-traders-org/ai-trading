#!/bin/bash

# port-forward
kubectl port-forward $(kubectl get pod -l app=mlflow -o jsonpath="{.items[0].metadata.name}") 5000:5000