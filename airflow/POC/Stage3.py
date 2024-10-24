import boto3
from botocore.exceptions import NoCredentialsError, ClientError 

def upload_to_s3(local_file, bucket, s3_file):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print (f"Upload Successful: {local_file} to s3://{bucket}/{s3_file}")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except ClientError as e:
        print("Client error: {e}")
        return False
    
    local_file = "cover_image.jpg"
    bucket = "ddddemo-damg7245-fall2024"
    s3_file = "cover_image.jpg"
    upload_to_s3(local_file, bucket, s3_file)
