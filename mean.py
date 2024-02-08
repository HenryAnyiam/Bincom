#!/usr/bin/python3
"""get the color of shirt which is the mean color"""


def replace(data: list, value: str, repl: int) -> list:
    while True:
        try:
            index = data.index(value)
        except ValueError:
            break
        else:
            data[index] = repl
    return data


def color_to_num(data: list) -> tuple:
    """convert colors to numbers"""
    color_num = 0
    color_dict = {}
    length = len(data)
    for i in range(length):
        if isinstance(data[i], str):
            color_dict[color_num] = data[i]
            data = data[0:i] + replace(data[i:], data[i], color_num)
            color_num += 1
    return data, color_dict


def get_mean(data: list) -> str:
    """calculate mean color"""
    convert_color = color_to_num(data)
    colors = convert_color[0]
    color_length = len(colors)
    avg = round(sum(colors) / color_length, 0)
    return convert_color[1][avg]


if __name__ == "__main__":
    from data import MERGED_DATA
    data = get_mean(MERGED_DATA)
    print(f"The color of the shirt which is the mean color is {data}")
