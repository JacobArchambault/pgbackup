from argparse import ArgumentParser
from pgbackup import driver_action

def create_parser():
    parser = ArgumentParser(description=""" 
    Back up PostgreSQL databases locally or to AWS S3
    """)
    parser.add_argument("url", help="URL of the database to backup")
    parser.add_argument("--driver", 
    '-d', 
    help="How and where to store backup", 
    nargs=2, 
    metavar=("DRIVER", "DESTINATION"),
    action=driver_action.DriverAction, 
    required=True)
    return parser
