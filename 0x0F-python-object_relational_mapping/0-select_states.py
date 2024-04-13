#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

def list_states(username, password, database):
    # connect to the MySQL server
    db = (host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute the SQL query to fetch all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the query result
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the database connection
    db.close()

    # Example usage
    if __name__ "" '__main__':
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        list_states(username, password, database)
        
