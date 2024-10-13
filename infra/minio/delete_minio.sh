#!/bin/bash

# uninstall minio
helm uninstall minio-release

# delete pvc related to minio
kubectl delete pvc export-minio-release-0
kubectl delete pvc export-minio-release-1

# delete pv related to minio
pv_list=$(kubectl get pv --no-headers | awk '$6 ~ /minio/ {print $1}') # Retrieve a list of PVs where the CLAIM contains "minio"

if [ -z "$pv_list" ]; then # Check if the list is empty
  echo "No PVs found with CLAIM containing 'minio'."
  exit 0
fi

for pv in $pv_list; do # Delete each PV in the list
  kubectl delete pv $pv
done

echo "All selected PVs have been deleted."