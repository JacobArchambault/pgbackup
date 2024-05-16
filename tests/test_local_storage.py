import pytest
from unittest.mock import patch, mock_open
from pgbackup import local_storage
from io import BytesIO

@patch('pgbackup.pgdump.dump')
@patch('builtins.open', new_callable=mock_open)
def test_backup(mock_open, mock_pgdump):
    # Arrange
    url = 'postgresql://user:password@localhost/dbname'
    destination = 'backup.sql'
    mock_pgdump.return_value = BytesIO(b'simulated database dump')

    # Act
    local_storage.backup(url, destination)

    # Assert
    mock_pgdump.assert_called_once_with(url)  # Ensure pgdump.dump was called with correct arguments
    mock_open.assert_called_once_with(destination, 'wb')
    handle = mock_open.return_value.__enter__.return_value
    handle.write.assert_called_once_with(b'simulated database dump') # Ensure the correct data was written