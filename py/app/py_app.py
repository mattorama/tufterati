#!/usr/bin/env python3

""" check module works """


def fun():
    """ check import of function """
    print("fun imported")
    return 23


def main():
    """ run from shell """
    _ = fun()


if __name__ == '__main__':
    main()
