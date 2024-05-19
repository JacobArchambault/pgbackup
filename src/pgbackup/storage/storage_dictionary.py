from pgbackup.storage import local_storage, s3_storage

driver_actions = {
    "s3": s3_storage.backup, 
    "local": local_storage.backup
}
