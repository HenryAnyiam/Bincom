#!/usr/bin/python3

def fibo(num):
    """generate a fibonacci"""

    arrays = [[1]]
    if num < 1:
        return []
    start = 0
    for i in range(1, num):
        new_arr = []
        for j in arrays[i - 1]:
            new_arr.append(j + start)
            start = j
        new_arr.append(start + 0)
        arrays.append(new_arr)
        start = 0
    return arrays


if __name__ == "__main__":
    fibos = fibo(5)
    for i in fibos:
        print(i)
