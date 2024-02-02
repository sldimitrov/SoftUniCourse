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


def login_user(c):
    # c is client
    # message = client.recv(1024).decode()
    # client.send(input(message).encode())
    # message = client.recv(1024).decode()
    # client.send(input(message).encode())
    # print(client.recv(1024).decode())

    c.send("Username: ".encode())
    username = c.recv(1024).decode()
    c.send("Password: ".encode())
    password = c.recv(1024)
    password = hashlib.sha256(password).hexdigest()

    conn = sqlite3.connect("userdata.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))

    if cur.fetchall():
        c.send("Login successful!".encode())
        # secrets
        # services
    else:
        c.send("Login failed!".encode)


# Read User input
command = input("reg or log: ")

# In case he doesn't exist in the database
if command == "reg":
    # Read User data
    user_name = input('name: ')
    user_pass = input('pass: ')

    if register_user(user_name, user_pass):
        print("User was registered.")

# In case he is already in the database
elif command == "log":
    login_user()

else:
    print(f"Unknown command {command}")

# Read Input from the User


