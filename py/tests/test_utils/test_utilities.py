""" test utils/utilities.py """

from utils.utilities import funbaz


def test_funbaz():
    """ test funbaz """

    expect = 2
    result = funbaz(1)
    assert result == expect

    expect = 4
    result = funbaz(2)
    assert result == expect


def main():
    """ execute tests from cli """
    test_funbaz()
    print("tests passed")


if __name__ == '__main__':
    main()
