""" test utils/db_utils.py """

from utils.db_utils import db_connect, sqlite_version_check


def test_sqlite_version_check():
    """ test sqlite_version_check """

    expect = [('3.30.1',)]
    con = db_connect(':memory:')
    result = sqlite_version_check(con)
    assert result == expect
