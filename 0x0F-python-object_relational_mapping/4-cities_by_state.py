#!/usr/bin/python3
""" Script that prints all the cities in MySQL database
    using the python connector MySQLdb
"""

import sys
import MySQLdb

if __name__ == '__main__':
    conet = MySQLdb.connect(
            user=sys.argv[1],
            host='localhost',
            port=3306,
            password=sys.argv[2],
            db=sys.argv[3]
            )
    cur = conet.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                ORDER BY cities.id ASC")
    data = cur.fetchall()
    for val in data:
        print(val)
    cur.close()
    conet.close()
