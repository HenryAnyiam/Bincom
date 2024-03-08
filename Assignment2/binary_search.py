#!/usr/bin/python3
"""Binary search implementation"""

def binary_search(array:list, value:int, start:int, end:int) -> int:
    """search a sorted array"""

    mid = (start + end) // 2
    if value == array[mid]:
        return mid
    if (len(array[start:end]) == 1 and array[mid] != value):
        return
    if array[mid] > value:
        return binary_search(array, value, start, mid)
    else:
        return binary_search(array, value, mid + 1, end)


if __name__ == "__main__":
    array = [2, 3, 6, 9, 15, 24]
    print(binary_search(array, 6, 0, len(array)))
