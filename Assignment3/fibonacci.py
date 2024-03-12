#!/usr/bin/python3
"""Implement a fibonacci sequesnce"""

def fibo(num: int) -> list:
    """generate a fibonacci the length of num"""

    if num < 1:
        return []
    arrays = [[1]]
    hold = 0

    for i in range(1, num):
        new_array = []
        for j in arrays[i - 1]:
            new_array.append(hold + j)
            hold = j
        new_array.append(hold + 0)
        hold = 0
        arrays.append(new_array)

    return arrays


if __name__ == "__main__":
    fibonacci = fibo(5)
    for i in fibonacci:
        print(i)
