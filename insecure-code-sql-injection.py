# examples of insecure code subject to injection attacks

import mysql.connector

def login(username, password):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='mydatabase')
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)

    result = cursor.fetchone()

    if result:
        print("Login successful")
    else:
        print("Login failed")

    cursor.close()
    conn.close()
