from argparse import Action, ArgumentParser
class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination=values
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser(description=""" 
    Back up PostgreSQL databases locally or to AWS S3
    """)
    parser.add_argument("url", help="URL of the database")
    parser.add_argument("--driver", help="How and where to store backup", nargs=2, action=DriverAction, required=True)
    return parser