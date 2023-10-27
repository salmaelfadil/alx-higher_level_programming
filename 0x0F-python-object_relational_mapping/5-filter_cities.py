#!/usr/bin/python3
"""
script that takes the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    state_name = sys.argv[4]
    cursor.execute("SELECT cities.name FROM cities JOIN states ON \
                    states.id=cities.state_id \
                    WHERE states.name=%s", (state_name,))
    rows = cursor.fetchall()
    lis = [row[0] for row in rows]
    lis_str = ', '.join(lis)
    print(lis_str)
    cursor.close()
    db.close()
