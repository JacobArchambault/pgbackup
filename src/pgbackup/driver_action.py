from argparse import Action

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination=values
        namespace.driver = driver.lower()
        namespace.destination = destination