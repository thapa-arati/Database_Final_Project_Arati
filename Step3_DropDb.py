import mysql.connector

# Establish connection to the MySQL server
connection = mysql.connector.connect(
    host="localhost",      # Replace with your MySQL server host
    user="root",   # Replace with your MySQL username
    password="4082"   # Replace with your MySQL password
)

if connection.is_connected():
    print("Connected to MySQL server")

    # Create a cursor object
    cursor = connection.cursor()

    # Drop the menagerie database if it exists
    cursor.execute("DROP DATABASE IF EXISTS menagerie")

    # Close the cursor and the connection
    cursor.close()
    connection.close()
    print("Disconnected from MySQL server")
