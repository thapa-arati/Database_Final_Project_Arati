import mysql.connector as mc
from tabulate import tabulate

conn= mc.connect(host='localhost',user='root',password='4082',db='menagerie')
def read_data():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pet')
    pet_records = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print(tabulate(pet_records, headers=headers, tablefmt="fancy_grid"))

def main():
   read_data()

if __name__ == '__main__':
   main()