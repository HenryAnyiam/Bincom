#!/usr/bin/python3
"""generate a binary and covert it to decimal"""


from random import randint

def bin_to_dec() -> tuple:
    num = ""
    for i in range(4):
        num = str(randint(0, 1)) + num

    dec = 0
    index = 3
    for i in range(4):
        dec += int(num[index]) * (2 ** i)
        index -= 1

    return num, dec


if __name__ == "__main__":
    values = bin_to_dec()
    print(f"Binary number {values[0]} is {values[1]} in decimal")
