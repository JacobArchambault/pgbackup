import boto3
from pgbackup import pgdump, timestamped_db_name

def backup(url, bucket):
    boto3.client('s3').upload_fileobj(
        pgdump.dump(url), 
        bucket, 
        timestamped_db_name.get(url))