
from pgbackup import storage, parser, local_storage

def main():
    args = parser.create_parser().parse_args()
    if args.driver == 's3':
        storage.s3(
            args.url, 
            args.destination)
    else:
        local_storage.backup(
            args.url, 
            args.destination)