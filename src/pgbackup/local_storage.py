from pgbackup import pgdump

def backup(url, destination):
    dumped = pgdump.dump(url)
    outfile = open(destination, 'wb')
    outfile.write(dumped)
    outfile.close()