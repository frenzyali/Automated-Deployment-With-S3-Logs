#!/bin/bash
LOG_FILE="/var/lib/docker/containers/*/*-json.log"
BUCKET_NAME="<YOUR BUCKET NAME>"
aws s3 cp $LOG_FILE s3://$BUCKET_NAME/docker-logs/ --recursive

