import psycopg2

def create_table():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="Abhi@202398",host="localhost",port="5432")

    cursor = conn.cursor()
    cursor.execute('''create table employees(Name Text, ID int, Programming Text, Age int);''')
    print("Table created successfully")
    conn.commit()
    conn.close()

def insert_data():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="Abhi@202398",host="localhost",port="5432")

    cursor = conn.cursor()
    name = input("Enter name: ")
    userId = int(input("Enter id: "))
    language = input("Enter programming language: ")
    age = int(input("Enter age: "))
    query = '''insert into employees(Name,ID,Programming,Age) values(%s,%s,%s,%s);'''
    cursor.execute(query,(name,userId,language,age))
    print("Data addd successfully")
   
    conn.commit()
    conn.close()

insert_data()