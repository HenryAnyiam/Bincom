#!/usr/bin/python3
"""get the median color"""


def get_median(data: list) -> str:
    """get median color"""
    return data[len(data) // 2]


if __name__ == "__main__":
    from data import MERGED_DATA
    median_color = get_median(MERGED_DATA)
    print(f"The median color is {median_color}")
