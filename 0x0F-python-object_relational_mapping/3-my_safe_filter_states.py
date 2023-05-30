#!/usr/bin/python3
"""script that takes in arguments and displays all values in the states table
in a way that is safe from MySQL injections"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    c = db.cursor()
    
    c.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY states.id ASC", (sys.argv[4],))
    
    rows = c.fetchall()  
    for row in rows:
        print(row)