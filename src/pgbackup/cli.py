
from pgbackup import storage, parser

def main():
    args = parser.create_parser().parse_args()
    if args.driver == 's3':
        storage.s3(
            args.url, 
            args.destination)
    else:
        storage.local(
            args.url, 
            args.destination)