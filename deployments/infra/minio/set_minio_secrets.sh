#!/bin/bash

# Check if the 'minio-credentials' secret exists
if kubectl get secret minio-credentials > /dev/null 2>&1; then
  echo "The 'minio-credentials' secret exists. Deleting it..."
  kubectl delete secret minio-credentials
else
  echo "The 'minio-credentials' secret does not exist. Proceeding..."
fi

# Create a secret with MinIO credentials
kubectl create secret generic minio-credentials \
  --from-literal=MINIO_ACCESS_KEY=$(kubectl get secret minio-release -o jsonpath='{.data.rootUser}' | base64 --decode) \
  --from-literal=MINIO_SECRET_KEY=$(kubectl get secret minio-release -o jsonpath='{.data.rootPassword}' | base64 --decode)

echo "The new 'minio-credentials' secret has been created."
