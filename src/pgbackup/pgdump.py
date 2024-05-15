from subprocess import Popen, PIPE
from sys import exit

def dump(url):
    try:
        return Popen(['pg_dump', url], stdout=PIPE).stdout
    except OSError as err:
        print(f"Error: {err}")
        exit(1)