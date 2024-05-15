from time import strftime, localtime

def get(url):
    return f"{url.split('/')[-1].split('?')[0]}-{strftime("%Y-%m-%dT%H:%M", localtime())}.sql"