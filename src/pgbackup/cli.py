
from pgbackup import pgdump, storage, parser

def main():

    args = parser.create_parser().parse_args()
    if args.driver == 's3':
        storage.s3(
            pgdump.dump(args.url), 
            args.destination, 
            pgdump.dump_file_name(args.url))
    else:
        storage.local(
            pgdump.dump(args.url), 
            open(args.destination, 'wb'))