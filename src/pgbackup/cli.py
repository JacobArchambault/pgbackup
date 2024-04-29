from argparse import ArgumentParser
from pgbackup import driver_action

def create_parser():
    parser = ArgumentParser(description=""" 
    Back up PostgreSQL databases locally or to AWS S3
    """)
    parser.add_argument("url", help="URL of the database")
    parser.add_argument("--driver", 
    '-d', 
    help="How and where to store backup", 
    nargs=2, 
    metavar=("DRIVER", "DESTINATION"),
    action=DriverAction, 
    required=True)
    return parser

def main():
    import boto3
    import time
    from pgbackup import pgdump, storage

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)
    if args.driver == 's3':
        client = boto3.client('s3')
        timestamp = time.strftime("%Y-%m-%dT%H:%M", time.localtime())
        file_name = pgdump.dump_file_name(args.url, timestamp)
        storage.s3(client, dump.stdout, args.destination, file_name)
    else:
        outfile = open(args.destination, 'wb')
        storage.local(dump.stdout, outfile)