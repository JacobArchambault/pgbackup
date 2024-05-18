from pgbackup.pgdump import dump
import pytest

url = "postgres://localhost/mydatabase"

class MockPopen:
    def __init__(self, *args, **kwargs):
        pass

    def communicate(self):
        return b"mocked stdout", b""

    @property
    def returncode(self):
        return 0

class MockPopenFailure:
    def __init__(self, *args, **kwargs):
        pass

    def communicate(self):
        return b"", b"mocked stderr" 

    @property
    def returncode(self):
        return 1

@pytest.fixture
def mock_popen_success(monkeypatch):
    monkeypatch.setattr("pgbackup.pgdump.Popen", MockPopen)

@pytest.fixture
def mock_popen_failure(monkeypatch):
    monkeypatch.setattr("pgbackup.pgdump.Popen", MockPopenFailure)

def test_dump_success(mock_popen_success):
    assert dump(url) == b"mocked stdout"

def test_dump_failure(mock_popen_failure):
    with pytest.raises(SystemExit) as excinfo:
        dump(url)
    assert "mocked stderr" in str(excinfo.value)
