
from pgbackup import pgdump, storage, parser

def main():

    args = parser.create_parser().parse_args()
    dump = pgdump.dump(args.url)
    if args.driver == 's3':
        storage.s3(
            dump.stdout, 
            args.destination, 
            pgdump.dump_file_name(args.url))
    else:
        storage.local(
            dump.stdout, 
            open(args.destination, 'wb'))