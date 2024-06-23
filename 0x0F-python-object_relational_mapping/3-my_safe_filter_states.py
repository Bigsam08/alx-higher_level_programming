#!/usr/bin/python3
""" script connects to base to search for states
    using user formatted inout
    %s used for safe from SQL injection
"""
import sys
import MySQLdb

if __name__ == "__main__":
    conet = MySQLdb.connect(
            user=sys.argv[1],
            host='localhost',
            port=3306,
            password=sys.argv[2],
            db=sys.argv[3]
            )
    cur = conet.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s\
                ORDER BY states.id ASC".format(sys.argv[4]))
    data = cur.fetchall()
    for val in data:
        print(val)
    cur.close()
    conet.close()
