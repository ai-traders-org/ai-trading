#!/bin/bash

# rootUser / access-key
echo "rootUser / access-key:"
kubectl get secret minio-release -o jsonpath='{.data.rootUser}' | base64 --decode
echo -e "\n"

# rootPassword / private-key
echo "rootPassword / private-key:"
kubectl get secret minio-release -o jsonpath='{.data.rootPassword}' | base64 --decode
echo -e "\n"
