#!/usr/bin/python3
"""A To Do List implementation"""

import psycopg2
import re

conn = psycopg2.connect("dbname=mac user=mac")
conn.autocommit = True
curr = conn.cursor()

curr.execute("SELECT 1 FROM pg_database WHERE datname = %s", ('to_do_db',))
database = curr.fetchone()

if not database:
    curr.execute("CREATE DATABASE to_do_db")

conn.commit()

curr.close()
conn.close()

conn = psycopg2.connect("dbname=to_do_db user=mac")
conn.autocommit = True
curr = conn.cursor()

curr.execute("SELECT 1 FROM information_schema.tables WHERE table_name = %s", ('to_do',))
table = curr.fetchone()

if not table:
    curr.execute("CREATE TABLE to_do (id SERIAL PRIMARY KEY, action VARCHAR, action_date VARCHAR, action_time VARCHAR);")

curr.execute("SELECT * FROM to_do;")
trial = 3

while True:

    print("""
    1: View To Do
    2: Add To Do
    3: Delete To Do
    4: Exit
    """)
    response = input("Pick an option: ")

    if response == "4" or response.lower() == "exit":
        print("Thank You")
        break
    elif response == "2" or response.lower() == "add to do":
        print("\n\nAdd a To Do\n")
        action = input("Input To Do: ")
        date = input("Input To Do Date format=DD/MM/YYYY: ")
        time = input("Input Time format=HH:MM: ")
        if (re.match("^\d?\d/\d{2}/\d{4}$", date) and 
                re.match("^\d?\d/\d{2}/\d{4}$", date) and action):
            curr.execute("INSERT INTO to_do (action, action_date, action_time) VALUES (%s, %s, %s)", (action, date, time))
        else:
            print("Invalid Input, Do Try Again")
    elif response == "1" or response.lower() == "view to do":
        curr.execute("SELECT * FROM to_do;")
        to_do_data = curr.fetchall()
        if to_do_data:
            print("YOUR TO DO")
        else:
            print("You Have nothing in your to do list currently")
        for i in to_do_data:
            print()
            print(f"TO DO {i[0]}")
            print(i[1].upper())
            print(f"Date: {i[2]}")
            print(f"Time: {i[3]}")
            print()
    elif response == "3" or response.lower() == "delete to do":
        curr.execute("SELECT * FROM to_do;")
        to_do_data = curr.fetchall()
        if to_do_data:
            print("YOUR TO DO")
        else:
            print("You Have nothing in your to do list currently")
        for i in to_do_data:
            print()
            print(f"ID {i[0]} {i[1].upper()}")
            print()
        delete = input("Please input the ID of the To Do you wish to delete: ")
        try:
            delete = int(delete)
        except ValueError:
            print(f"Invalid Input, You have no to do with an id of {delete}")
        else:
            curr.execute("SELECT 1 FROM to_do  WHERE id = %s", (delete, ))
            data = curr.fetchone()
            if data:
                ask = input(f"Are you sure you want to delete {data[0]} (yes/no): ")
                if ask.lower() == "yes":
                    curr.execute("DELETE FROM to_do WHERE id = %s", (delete, ))
                    print("Successfully Deleted")
                else:
                    print("Not Deleted")
            else:
                print(f"Invalid Input, You have no to do with an id of {delete})
