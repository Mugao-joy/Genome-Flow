import os
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError

S3_ENDPOINT = os.getenv("S3_ENDPOINT")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")
BUCKET_NAME = os.getenv("S3_BUCKET")

s3 = boto3.client(
    "s3",
    endpoint_url=S3_ENDPOINT,
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
    config=Config(
        s3={"addressing_style": "path"},
        signature_version="s3v4",
    ),
    region_name="us-east-1",
)

def ensure_bucket_exists():
    try:
        s3.head_bucket(Bucket=BUCKET_NAME)
    except ClientError as e:
        error_code = int(e.response["Error"]["Code"])
        if error_code == 404:
            s3.create_bucket(Bucket=BUCKET_NAME)
        else:
            raise

# 👇 run once on import
ensure_bucket_exists()

def upload_file(file_obj, object_name: str):
    s3.upload_fileobj(file_obj, BUCKET_NAME, object_name)

def get_file_url(object_name: str):
    return f"{S3_ENDPOINT}/{BUCKET_NAME}/{object_name}"
