#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_0_usa that belong to a specific state."""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = db.cursor()

    cursor.execute("""
        SELECT cities.name FROM cities
        INNER JOIN states ON states.id = cities.state_id
        WHERE states.name = %s
    """, (sys.argv[4],))

    rows = cursor.fetchall()

    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    cursor.close()
    db.close()
