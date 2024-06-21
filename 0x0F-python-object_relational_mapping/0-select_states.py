#!/usr/bin/python3
""" a script that lists all the states im a database """

import MySQLdb
import sys

if __name__ == ' __main__':
    conet = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3],
            )
    cur = conet.cursor()
    cur.execute("SELECT * FROM states ORDERED BY id ASC;")
    rows = cur.fetchall()
    for r in rows:
        print(r)

    cur.close()
    conet.close()
