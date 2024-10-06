#!/bin/bash

# make secret with minio credentials
kubectl create secret generic minio-credentials --from-literal=MINIO_ACCESS_KEY=$(kubectl get secret minio-release -o jsonpath='{.data.rootUser}' | base64 --decode) --from-literal=MINIO_SECRET_KEY=$(kubectl get secret minio-release -o jsonpath='{.data.rootPassword}' | base64 --decode)
