import math
import numpy as np


def main():
    N = int(input())

    if(N % 2 == 1):
        return

    left = N // 2
    opened = 0
    result = func("", 0, left)

    for s in result:
        print(s)


def func(s, opened, left):  # opened + left = N // 2
    if(opened == 0 and left == 0):
        return [s]

    result = []
    if(left != 0):
        result += func(s + "(", opened + 1, left - 1)
    if(opened != 0):
        result += func(s + ")", opened - 1, left)

    return result


if(__name__ == "__main__"):
    main()
