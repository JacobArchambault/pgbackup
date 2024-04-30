import boto3

def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()

def s3(infile, bucket, name):
    boto3.client('s3').upload_fileobj(infile, bucket, name)