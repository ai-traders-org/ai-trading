#!/bin/bash

# run job
kubectl delete job download-data-job
kubectl apply -f deployments/data/download_data/job.yaml