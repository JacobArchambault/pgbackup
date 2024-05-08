from pgbackup import pgdump

def backup(url, destination):
    outfile = open(destination, 'wb')
    infile = pgdump.dump(url)
    outfile.write(infile.read())
    outfile.close()
    infile.close()