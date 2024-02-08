#!/usr/bin/python3
"""save data to postgresql"""


import psycopg
from os import getenv


def calculate_frquency(data: list) -> dict:
    """calculate frequency of each colors"""
    frequency = {}
    color = ""
    for i in data:
        if i not in frequency:
            count = data.count(i)
            frequency[i] = count
    return frequency


def save_data(data: list) -> None:
    """save data"""
    frequency = calculate_frequency(data)
    with psycopg.connect(f"db_name={getenv('DB')} user={getenv('USER')}") as conn:

        with conn.cursor() as cursor:

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS colors (
                    id serial PRIMARY KEY,
                    color text,
                    count integer)
                """)

            for i in frequency:
                cursor.execute(
                    "INSERT INTO colors (color, count) VALUES (%s, %s)",
                    (i, frequency[i]))
            conn.commit()
    return


if __name__ == "__main__":
    from data import MERGED_DATA
    try:
        val = save_data(MERGED_DATA)
    except Error as e:
        print(e)
    else:
        if not val:
            print("Saved Successfully")
