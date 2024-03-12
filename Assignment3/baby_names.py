#!/usr/bin/python3
"""use regular expression to extract baby names from an html file"""

import psycopg2
import re

with open("baby2008.html", "r", encoding="utf-8") as my_file:
    data = my_file.read()


result = re.findall("(?<=<td>)[A-Z][a-z]+", data)
male_names = [result[i] for i in range(0, len(result), 2)]
female_names = [result[i] for i in range(1, len(result), 2)]

conn = psycopg2.connect("dbname=to_do_db user=mac")
conn.autocommit = True
curr = conn.cursor()

curr.execute("SELECT 1 FROM information_schema.tables WHERE table_name = %s", ('male_baby_names',))
table = curr.fetchone()

if not table:
    curr.execute("CREATE TABLE male_baby_names (id SERIAL PRIMARY KEY, name VARCHAR);")

curr.execute("SELECT 1 FROM information_schema.tables WHERE table_name = %s", ('female_baby_names',))
table = curr.fetchone()

if not table:
    curr.execute("CREATE TABLE female_baby_names (id SERIAL PRIMARY KEY, name VARCHAR);")

for i in male_names:
    curr.execute("INSERT INTO male_baby_names (name) VALUES (%s)", (i,))

for i in male_names:
    curr.execute("INSERT INTO male_baby_names (name) VALUES (%s)", (i,))
