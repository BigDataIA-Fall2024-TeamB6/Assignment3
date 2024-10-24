import boto3
from botocore.exceptions import NoCredentialsError, ClientError 

def upload_to_s3(local_file, bucket, s3_file):
    #s3 = boto3.client('s3')
    s3 = boto3.client('s3', aws_access_key_id='AKIAU6GD3H5T44SFJJV2', aws_secret_access_key='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')
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
    
    local_file = "/Users/ramyyogeshkumarsolanki/Documents/GitHub/Assignment3/airflow/POC/Stage3.py"
    bucket = "ddddemo-damg7245-fall2024"
    s3_file = "cover_image.jpg"
    upload_to_s3(local_file, bucket, s3_file)
