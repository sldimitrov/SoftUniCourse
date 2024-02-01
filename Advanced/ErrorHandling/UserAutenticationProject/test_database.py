import sqlite3
import hashlib


def register_user(name, user_password):
    # Connect to the database
    conn = sqlite3.connect("userdata.db")
    cur = conn.cursor()

    # Add a column to the table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS userdata (
        id INTEGER PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
    """)

    # Parse the username and password into bytes
    username, password = name, hashlib.sha256(user_password.encode()).hexdigest()

    # Insert data into the database
    cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username, password))

    # Commit the changes
    conn.commit()

    return True


# Read Input from the User
user_name = input('name: ')
user_pass = input('pass: ')

# If the func returns True print out a message
if register_user(user_name, user_pass):
    print('User was registered.')

