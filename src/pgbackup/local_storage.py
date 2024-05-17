from pgbackup import pgdump

def backup(url, destination):
    dumped_data = pgdump.dump(url)
    with open(destination, 'wb') as outfile:
        outfile.write(dumped_data)
