import boto3
from pgbackup import pgdump

def s3(url, bucket):
    infile = pgdump.dump(url)
    name = pgdump.dump_file_name(url)
    boto3.client('s3').upload_fileobj(infile, bucket, name)