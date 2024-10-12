#!/bin/bash

# install minio
helm install minio-release minio/minio -f ./deployments/infra/minio/values.yaml