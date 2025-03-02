#!/bin/bash
BUCKET_NAME="<YOUR BUCKET NAME>"
aws s3 cp /var/lib/docker/containers/ s3://$BUCKET_NAME/docker-logs/ --recursive --exclude '*' --include '*.log'
