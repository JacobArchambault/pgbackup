from subprocess import Popen, PIPE
from sys import exit
from time import strftime, localtime

def dump(url):
    try:
        return Popen(['pg_dump', url], stdout=PIPE).stdout
    except OSError as err:
        print(f"Error: {err}")
        exit(1)

def dump_file_name(url):
    return f"{url.split('/')[-1].split('?')[0]}-{strftime("%Y-%m-%dT%H:%M", localtime())}.sql"