from pgbackup import s3_storage, local_storage

driver_actions = {
    "s3": s3_storage.backup, 
    "local": local_storage.backup
}
