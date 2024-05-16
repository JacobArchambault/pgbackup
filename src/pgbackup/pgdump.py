from subprocess import Popen, PIPE
from sys import exit

def dump(url):
    try:
        process = Popen(['pg_dump', url], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            raise OSError(f"pg_dump failed with return code {process.returncode}. Error message: {stderr.decode()}")
        return stdout
    except OSError as err:
        raise SystemExit(f"Error: {err}")
