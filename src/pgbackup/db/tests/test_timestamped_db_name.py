from pgbackup.db import timestamped_db_name

url = "postgres://bob:password@example.com:5432/db_one?connect_timeout=10"

def test_timestamped_db_name_returns_db_name_as_sql_file():
    """
    timestamped_db_name.get returns a .sql file name beginning with the name of the database
    """
    timestamped = timestamped_db_name.get(url)
    assert timestamped.startswith("db_one")
    assert timestamped.endswith(".sql")

def test_timestamped_db_name_removes_query_params():
    """
    timestamped_db_name.get removes query params from the end of a postgres URL
    """
    timestamped = timestamped_db_name.get(url)
    assert "connect_timeout" not in timestamped
    assert "?" not in timestamped
