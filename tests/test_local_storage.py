import pytest
from pgbackup import local_storage
from io import BytesIO

url = 'postgresql://user:password@localhost/dbname'
destination = 'backup.sql'

def test_backup(mocker):
    # Arrange
    mock_pgdump = mocker.patch('pgbackup.pgdump.dump')
    mock_open = mocker.patch('builtins.open', mocker.mock_open())
    mock_pgdump.return_value = BytesIO(b'simulated database dump')

    # Act
    local_storage.backup(url, destination)

    # Assert
    mock_pgdump.assert_called_once_with(url)  # Ensure pgdump.dump was called with correct arguments
    handle = mock_open()
    handle.write.assert_called_once_with(b'simulated database dump') # Ensure the correct data was written