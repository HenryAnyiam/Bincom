#!/usr/bin/python3
"""get the color mostly worn throughout the week"""


def get_mode(data: list) -> str:
    """get mode color"""
    counted = []
    most = float('-inf')
    color = ""
    for i in data:
        if i not in counted:
            counted.append(i)
            count = data.count(i)
            if count > most:
                most = count
                color = i
    return color


if __name__ == "__main__":
    from data import MERGED_DATA
    mode_color = get_mode(MERGED_DATA)
    print(f"The color mostly worn throughout the week is {mode_color}")
