#!/usr/bin/python3
"""
    A python MySQLdb script to connect to MySQL database
    print all states starting with 'N' only
"""

import MySQLdb
import sys


if __name__ == '__main__':
    conet = MySQLdb.connect(
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3],
            host='localhost',
            port=3306
            )
    cur = conet.cursor()
    cur.execute("SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id ASC")
    data = cur.fetchall()
    for r in data:
        print(r)

    cur.close()
    conet.close()
