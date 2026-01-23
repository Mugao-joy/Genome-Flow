import os
import boto3
from dotenv import load_dotenv

load_dotenv()

S3_ENDPOINT = os.getenv("S3_ENDPOINT")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")
BUCKET_NAME = os.getenv("S3_BUCKET")

s3 = boto3.client(
    "s3",
    endpoint_url=S3_ENDPOINT,
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
)

def upload_file(file_obj, object_name: str):
    s3.upload_fileobj(file_obj, BUCKET_NAME, object_name)

def get_file_url(object_name: str):
    return f"{S3_ENDPOINT}/{BUCKET_NAME}/{object_name}"
