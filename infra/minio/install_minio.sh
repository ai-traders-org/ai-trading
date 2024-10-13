#!/bin/bash

# install minio
helm install minio-release minio/minio -f ./infra/minio/values.yaml