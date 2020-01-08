#!/usr/bin/env python3
""" check sqlite3 connection

https://pynative.com/python-sqlite/

"""

import os
import sqlite3

# create a default path to connect to and create (if necessary) a database
# called 'database.sqlite3' in the same directory as this script
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')


def db_connect(db_path=DEFAULT_PATH):
    """ db connection """
    con = sqlite3.connect(db_path)
    return con


def sqlite_version_check(con):
    """ get the sqlite version """
    cursor = con.cursor()
    res = cursor.execute("SELECT sqlite_version();").fetchall()
    print("SQLite Database Version is: ", res)
    cursor.close()
    return res


def check_sqlite3():
    """ module """
    try:
        sqlite_conn = sqlite3.connect(':memory:')
        cursor = sqlite_conn.cursor()
        print("Database created and Successfully Connected to SQLite")

        sqlite_select_query = "select sqlite_version();"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        print("SQLite Database Version is: ", record)
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqlite_conn:
            sqlite_conn.close()
            print("The SQLite connection is closed")


if __name__ == '__main__':
    check_sqlite3()
