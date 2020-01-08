#!/usr/bin/env python3
""" check sqlite3 connection

https://pynative.com/python-sqlite/

"""

import os
import sqlite3

import pandas as pd

from utils.db_utils import db_connect, sqlite_version_check


def create_lineitems_table(con):
    """ need a table """
    cur = con.cursor()
    lineitems_sql = """
        CREATE TABLE lineitems (
            id integer PRIMARY KEY,
            quantity integer NOT NULL,
            total real NOT NULL,
            product_id integer,
            order_id integer,
            FOREIGN KEY (product_id) REFERENCES products (id),
            FOREIGN KEY (order_id) REFERENCES orders (id))"""
    cur.execute(lineitems_sql)


def create_lineitem(con, order_id, product_id, qty, total):
    """ insert values into table """
    sql = """
        INSERT INTO lineitems
            (order_id, product_id, quantity, total)
        VALUES (?, ?, ?, ?)"""
    cur = con.cursor()
    cur.execute(sql, (order_id, product_id, qty, total))
    return cur.lastrowid


def create_table_and_query(con):
    """ how to create and query """
    try:
        create_lineitems_table(con)
        create_lineitem(con, 1, 100, 13, 26)
        create_lineitem(con, 2, 100, 14, 28)
        create_lineitem(con, 1, 120, 12, 36)
        create_lineitem(con, 3, 120, 13, 39)
        con.commit()
    except sqlite3.Error:
        con.rollback()
    cur = con.cursor()
    cur.execute("SELECT * FROM lineitems;")
    res = cur.fetchall()
    for row in res:
        print(row)


def main():
    """ check utils work """

    # connect to in-memory database
    con = db_connect(':memory:')

    # check sqlite version
    _ = sqlite_version_check(con)

    # create a table and query the content
    create_table_and_query(con)

    # read a csv into a table and query the content
    csv_path = os.path.join(os.environ['DATA_PATH'], 'mock1.csv')
    df_1 = pd.read_csv(csv_path)
    df_1.to_sql('mock', con, if_exists='append', index=False)

    # return the results of a query read from a text file
    query_path = os.path.join(os.environ['DATA_PATH'], 'sqlite_query.sql')
    with open(query_path, 'r') as obj:
        sql_query = obj.read()
    df_2 = pd.read_sql(sql_query, con)
    print(df_2)


if __name__ == '__main__':
    main()
