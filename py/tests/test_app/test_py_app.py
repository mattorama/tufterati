""" test app/py_app.py """

from app.py_app import fun


def test_fun():
    """ test fun """

    expect = 23
    result = fun()
    assert result == expect
