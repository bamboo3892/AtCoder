import math
import numpy as np


def main():
    N = int(input())
    DCS = [list(map(int, input().split())) for _ in range(N)]
    DCS.sort(key=lambda x: x[0])

    max_value = 0
    for bit in range(pow(2, N)):
        l = func(bit, N)
        date = 0
        value = 0
        for i in l:
            date += DCS[i][1]
            if(date > DCS[i][0]):
                break
            value += DCS[i][2]
        max_value = max([max_value, value])

    print(max_value)


def func(bit, N):
    rtn = []
    for n in range(N):
        if(((bit >> n) & 1) == 1):
            rtn.append(n)
    return rtn


if(__name__ == "__main__"):
    main()
