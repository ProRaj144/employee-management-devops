import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "employee-management-s3-bucket"

s3 = boto3.client("s3")


def upload_file(file_obj, filename):
    try:
        s3.upload_fileobj(file_obj, BUCKET_NAME, filename)
        return f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"
    except ClientError as e:
        raise Exception(str(e))


def list_files():
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    files = []

    if "Contents" in response:
        for obj in response["Contents"]:
            files.append({"name": obj["Key"], "size": obj["Size"]})

    return files


def delete_file(filename):
    s3.delete_object(Bucket=BUCKET_NAME, Key=filename)
