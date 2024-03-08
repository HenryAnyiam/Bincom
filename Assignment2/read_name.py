#!/usr/bin/python3
"""read names from a text file"""

with open("name.txt", "r", encoding="utf-8") as my_file:
    line = my_file.read()
    names = line.split()
    name = { "Last Name": names[0],
            "First Name": names[1],
            "Middle Name": names[2]}
    print(name)
