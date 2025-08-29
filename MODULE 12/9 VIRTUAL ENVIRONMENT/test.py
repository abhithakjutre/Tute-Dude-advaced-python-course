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
    cursor.execute('''insert into employees(Name,ID,Programming,Age) values('abhicoder', 25, 'python', 19);''')
    print("Data inserted successfully")
   
    conn.commit()
    conn.close()

def extract_data():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="Abhi@202398",host="localhost",port="5432")
    
    cursor = conn.cursor()
    cursor.execute('''select * from employees;''')
    show = cursor.fetchone()
    print(show)
    print(show[0])
    print(show[1])
    print(show[2])
    print(show[3])

    conn.commit()
    conn.close()
extract_data()