#!/bin/bash

# install minio
helm install minio-release minio/minio -f ./deployments/data/minio/values.yaml