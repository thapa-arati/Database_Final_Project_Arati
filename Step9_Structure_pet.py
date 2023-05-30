import mysql.connector
# Establish connection to the MySQL server
connection = mysql.connector.connect(
    user="root",
    password="4082",  # Replace with your MySQL password
    database="menagerie"   # Replace with the name of your MySQL database
)

if connection.is_connected():
    print("Connected to MySQL server")
    # Create a cursor object
    cursor = connection.cursor()
    # Retrieve the structure of the pet table
    cursor.execute("DESCRIBE pet")
    # Fetch all the columns and their information
    table_structure = cursor.fetchall()
    # Print the structure of the pet table
    print("Structure of the pet table:")
    for column_info in table_structure:
        print(column_info)
    # Close the cursor and the connection
    cursor.close()
    connection.close()
    print("Disconnected from MySQL server")
