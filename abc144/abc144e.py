import math
import numpy as np


def main():
    s = input().split(" ")
    N = int(s[0])
    K = int(s[1])
    A = np.array([int(a) for a in input().split(" ")])
    F = np.array([int(a) for a in input().split(" ")])
    A = np.sort(A)
    F = np.sort(F)[::-1]
    AF = A * F
    m = np.max(AF)

    if(func(0, AF, F, N, K)):
        print(0)
        return
    a = 0
    b = m
    for aaa in range(m):
        if((b - a) <= 1):
            print(b)
            return
        mid = int((b - a) / 2.) + a
        if(func(mid, AF, F, N, K)):
            b = mid
        else:
            a = mid
    print("???????")


def func(saidai, AF, F, N, K):
    count = np.sum(np.ceil((AF[(AF - saidai) > 0] - saidai) / F[(AF - saidai) > 0]))
    return count <= K


if(__name__ == "__main__"):
    main()
