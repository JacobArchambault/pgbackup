import boto3
from pgbackup import pgdump

def local(url, outfile):
    infile = pgdump.dump(url)
    outfile.write(infile.read())
    outfile.close()
    infile.close()

def s3(url, bucket):
    infile = pgdump.dump(url)
    name = pgdump.dump_file_name(url)
    boto3.client('s3').upload_fileobj(infile, bucket, name)