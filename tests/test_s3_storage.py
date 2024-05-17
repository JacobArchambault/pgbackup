import pytest
from unittest.mock import patch, MagicMock
from io import BytesIO
from pgbackup.s3_storage import backup

@patch('pgbackup.s3_storage.client')
@patch('pgbackup.s3_storage.pgdump.dump')
@patch('pgbackup.s3_storage.timestamped_db_name.get')
def test_backup(mock_get, mock_dump, mock_client):
    # Arrange
    mock_dump.return_value = b"mocked pg_dump data"
    mock_get.return_value = "mocked-db-name"
    mock_s3_client = MagicMock()
    mock_client.return_value = mock_s3_client

    url = "postgres://localhost/mydatabase"
    bucket = "mybucket"

    # Act
    backup(url, bucket)

    # Assert
    mock_dump.assert_called_once_with(url)
    mock_get.assert_called_once_with(url)
    mock_client.assert_called_once_with('s3')
    mock_s3_client.upload_fileobj.assert_called_once()
    args, kwargs = mock_s3_client.upload_fileobj.call_args
    assert isinstance(args[0], BytesIO)  # Ensure the first argument is a BytesIO object
    assert args[1] == bucket
    assert args[2] == "mocked-db-name"
