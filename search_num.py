#!/usr/bin/python3
"""search for number in a list of numbers"""


def binary_search(num_list: list, num: int) -> int:
    length = len(num_list)
    if (length == 0 or (length == 1 and num != num_list[0])):
        return None
    mid = len(num_list) // 2
    if num == num_list[mid]:
        return num, mid
    if num > num_list[mid]:
        return binary_search(num_list[mid + 1:], num)
    else:
        return binary_search(num_list[:mid], num)


def start_search(num_list: list, num: int) -> int:
    """sort a list and start search"""
    num_list.sort()
    return binary_search(num_list, num)
