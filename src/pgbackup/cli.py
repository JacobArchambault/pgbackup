
from pgbackup import driver_action_dictionary, parser


def main():
    args = parser.create_parser().parse_args()
    driver_action_dictionary.driver_actions[args.driver](args.url, args.destination)