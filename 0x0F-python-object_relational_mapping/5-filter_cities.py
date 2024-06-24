#!/usr/bin/python3
""" Script that prints all the cities of a state in MySQL database
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
    cur.execute("SELECT cities.name\
                FROM cities INNER JOIN states ON cities.state_id=states.id\
                WHERE states.name=%s\
                ORDER BY cities.id ASC", (sys.argv[4],))
    data = cur.fetchall()
    print(*[val[0] for val in data], sep=', ')
    cur.close()
    conet.close()
