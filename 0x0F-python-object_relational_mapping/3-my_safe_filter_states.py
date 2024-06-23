#!/usr/bin/python3
import MySQLdb
from sys import argv

'''
script that lists all states from the database
'''
if __name__ == "__main__":
    dbs = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name)
    cursor = dbs.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
        (argv[4],)
        )
    db = cursor.fetchall()
    for i in db:
        print(i)
