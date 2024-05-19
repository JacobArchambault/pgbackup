from boto3 import client
from io import BytesIO
from pgbackup.db import pgdump, timestamped_db_name

def backup(url, bucket):
    with BytesIO(pgdump.dump(url)) as data:
        client('s3').upload_fileobj(
            data, 
            bucket, 
            timestamped_db_name.get(url))