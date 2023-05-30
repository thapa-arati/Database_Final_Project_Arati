import mysql.connector as mc
# Connect to the database
conn = mc.connect(host='localhost', user='root', password='4082', db='menagerie')
c = conn.cursor()  # Cursor to perform operations
def create_table():
    c.execute('DROP TABLE IF EXISTS pet')
    c.execute('''CREATE TABLE pet (
        name VARCHAR(20) NOT NULL UNIQUE,
        owner VARCHAR(20),
        species VARCHAR(20),
        sex CHAR(1),
        birth DATE,
        death DATE 
    )''')
def commit_close():
    conn.commit()
    c.close()
    conn.close()

def main():
    create_table()
    commit_close()


if __name__ == '__main__':
    main()
