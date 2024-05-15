from boto3 import client
from pgbackup import pgdump, timestamped_db_name

def backup(url, bucket):
    client('s3').upload_fileobj(
        pgdump.dump(url), 
        bucket, 
        timestamped_db_name.get(url))