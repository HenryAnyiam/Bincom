#!/usr/bin/python3
"""calculate the probability of picking a color"""


def calc_probability(color: str, data: list) -> int:
    count = data.count(color)
    length = len(data)
    probability = round((count / length) * 100, 2)
    return probability


if __name__ == "__main__":
    from data import MERGED_DATA
    probability = calc_probability('RED', MERGED_DATA)
    print(f"The probability of picking RED is {probability}%")
