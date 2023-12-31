#!/usr/bin/python3
"""
script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        if row[1][0] != 'N':
            pass
        print(row)
    cursor.close()
    db.close()
