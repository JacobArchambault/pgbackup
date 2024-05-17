from boto3 import client
from pgbackup import timestamped_db_name, pgdump
from io import BytesIO

def backup(url, bucket):
    with BytesIO(pgdump.dump(url)) as data:
        client('s3').upload_fileobj(
            data, 
            bucket, 
            timestamped_db_name.get(url))