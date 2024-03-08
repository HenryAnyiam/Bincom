#!/usr/bin/python3
"""get dress data"""

from bs4 import BeautifulSoup


def get_question_data() -> dict:
    """retrive data from given html file"""
    with open("./python_class_question.html", 'r', encoding='UTF-8') as my_file:
        html_data = my_file.read()

    soup = BeautifulSoup(markup=html_data, features="html.parser")

    data = soup.select(selector="td")
    refined_data = [i.get_text() for i in data]
    length = len(refined_data)
    final_data = {
            refined_data[i]: refined_data[i + 1].split(', ') for i in range(0, length, 2)
            }
    return final_data


def merge_all(data: dict) -> list:
    """merge a dictionary of list"""
    all_lists = []
    for i in data:
        all_lists.extend(data[i])
    return all_lists


FINAL_DATA = get_question_data()
MERGED_DATA = merge_all(FINAL_DATA)
