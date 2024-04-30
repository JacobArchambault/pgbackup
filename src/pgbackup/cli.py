
from pgbackup import pgdump, storage, parser

def main():

    args = parser.create_parser().parse_args()
    dump = pgdump.dump(args.url)
    if args.driver == 's3':
        storage.s3(
            dump, 
            args.destination, 
            pgdump.dump_file_name(args.url))
    else:
        storage.local(
            dump, 
            open(args.destination, 'wb'))