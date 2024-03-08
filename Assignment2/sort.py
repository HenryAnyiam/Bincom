#!/usr/bin/python3
"""sort an array of integers using the merge sort algorithm"""


def merge(array:list, start:int, mid:int, end:int) -> None:
    """merge array"""
    left_arr = array[start:mid + 1]
    right_arr = array[mid + 1:end + 1]

    i, j, k = 0, 0, start
    left, right = len(left_arr), len(right_arr)
    while i < left and j < right:
        if left_arr[i] < right_arr[j]:
            array[k] = left_arr[i]
            i += 1
        else:
            array[k] = right_arr[j]
            j += 1
        k += 1
    while i < left:
        array[k] = left_arr[i]
        i += 1
        k += 1
    while j < right:
        array[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort(array:list, start:int, end:int) -> None:
    """recursively split the array"""

    if start < end:
        mid = (start + end) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid + 1, end)
        merge(array, start, mid, end)


def start_sort(array:list) -> None:
    """call the recursive function"""
    length = len(array)
    merge_sort(array, 0, length)


if __name__ == "__main__":
    arr = [8, 3, 1, 7, 2, 2]
    print(arr)
    start_sort(arr)
    print(arr)
