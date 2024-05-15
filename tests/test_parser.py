import pytest

from pgbackup import parser

url = "postgres://bob@example.com:5432/db_one"

@pytest.fixture
def pgparser():
    return parser.create_parser()

def test_parser_without_driver(pgparser):
    """
    Without a specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        pgparser.parse_args([url])

def test_parser_with_driver(pgparser):
    """
    The parser will exit if it receives a driver without a destination
    """
    with pytest.raises(SystemExit):
        pgparser.parse_args([url, "--driver", "local"])

def test_parser_with_unknown_driver(pgparser):
    """
    The parser will exit if the driver name is unknown.
    """
    with pytest.raises(SystemExit):
        pgparser.parse_args([url, '--driver', 'azure', 'destination'])

def test_parser_with_known_drivers(pgparser):
    """
    The Parser will not exit if the driver name is known.
    """
    for driver in ['local', 's3']:
        assert pgparser.parse_args([url, '--driver', driver, 'destination'])

def test_parser_with_driver_and_destination(pgparser):
    """
    The parser will not exit if it receives a driver and destination
    """
    args = pgparser.parse_args([url, '--driver', 'local', '/some/path'])

    assert args.url == url
    assert args.driver == 'local'
    assert args.destination == '/some/path'
