import subprocess
import sys
import time

def dump(url):
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)

def dump_file_name(url):
    return f"{url.split('/')[-1].split('?')[0]}-{time.strftime("%Y-%m-%dT%H:%M", time.localtime())}.sql"