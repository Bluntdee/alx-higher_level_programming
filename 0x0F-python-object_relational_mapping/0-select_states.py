#!/usr/bin/python3
<<<<<<< HEAD
"""Lists states"""
=======

"""
lists all states from the database hbtn_0e_0_usa
"""
>>>>>>> 643653f5f799640582e021b490799985cf16eddb

import MySQLdb
from sys import argv

<<<<<<< HEAD
if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
@@ -14,3 +22,21 @@
        print(row)
    cur.close()
    conn.close()
=======

def get_states(username, password, dbname):
    """lists all states from the database hbtn_0e_0_usa"""
    db = MySQLdb.connect(host="localhost", port=3306, user=str(username),
                         passwd=str(password), db=str(dbname), charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    get_states(argv[1], argv[2], argv[3])
>>>>>>> 643653f5f799640582e021b490799985cf16eddb
