#!/usr/bin/python3
"""sum first 50 fibonacci"""


def fibo_sum():
    fibo = [[1]]
    sequence = [1]

    index = 0
    while len(sequence) < 50:
        hold = 0
        new = []
        for i in fibo[index]:
            new.append(hold + i)
            hold = i
        new.append(hold + 0)
        fibo.append(new)
        sequence.extend(new)
        index += 1
    final_sum = sum(sequence[:50])
    return final_sum


if __name__ == "__main__":
    solution = fibo_sum()
    print(f"The sum of the first 50 fibonacci sequence is {solution}")
