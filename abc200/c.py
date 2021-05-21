import math
import numpy as np


def main():
    N = int(input())
    A = [int(a) for a in input().split(" ")]

    l = [0] * 200
    for a in A:
        l[a % 200] += 1

    result = 0
    for i in l:
        result += i * (i - 1) // 2
    print(result)


if(__name__ == "__main__"):
    main()
