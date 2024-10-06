#!/bin/bash

# uninstall minio
helm uninstall minio-release

# delete pvc related to minio
kubectl delete pvc export-minio-release-0
kubectl delete pvc export-minio-release-1

# delete pv related to minio
#TODO!