#!/bin/bash

helm install minio-release minio/minio -f values.yaml

kubectl delete job download-data-job
kubectl apply -f job.yaml