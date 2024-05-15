from argparse import Action

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination=values
        if driver.lower() not in ['local', 's3']:
            parser.error("Unknown driver. Available drivers are 'local' & 's3'")
        namespace.driver = driver.lower()
        namespace.destination = destination