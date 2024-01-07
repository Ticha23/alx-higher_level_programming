#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

def list_states():
    """
    List all states from the database hbtn_0e_0_usa.

    Returns:
        None
    """
    # Replace 'root' and '38487102@MMg' with your actual MySQL username and password
    username = 'root'
    password = '38487102@MMg'
    database = 'hbtn_0e_0_usa'

    # Connect to the MySQL database
    connection = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute the SQL query to retrieve states
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Fetch and display results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and connection
    cursor.close()
    connection.close()

if __name__ == "__main__":
    """
    Entry point when the script is run.
    """
    list_states()

