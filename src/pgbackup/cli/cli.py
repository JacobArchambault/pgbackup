from pgbackup.storage import storage_dictionary 
from pgbackup.cli import parser


def main():
    args = parser.create_parser().parse_args()
    storage_dictionary.driver_actions[args.driver](args.url, args.destination)