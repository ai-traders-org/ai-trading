#!/bin/bash

# port-forward
kubectl port-forward minio-release-0 9000:9000 9001:9001 --namespace default