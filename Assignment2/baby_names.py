#!/usr/bin/python3

import re

with open("baby2008.html", "r", encoding="utf-8") as my_file:
    data = my_file.read()


result = re.findall("(?<=<td>)[A-Z][a-z]+", data)
male_names = [result[i] for i in range(0, len(result), 2)]
female_names = [result[i] for i in range(1, len(result), 2)]
print(f"Male Baby Names: {male_names}")
print(f"Female Baby Names: {female_names}")
