import boto3
import json

s3 = boto3.client('s3')

response = s3.put_object()
