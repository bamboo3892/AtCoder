import math
import numpy as np


def main():
    x = [int(a) for a in input().split(" ")]
    N = x[0]
    L = x[1]
    K = int(input())
    A = [0] + [int(a) for a in input().split(" ")] + [L]
    lengths = [A[n + 1] - A[n] for n in range(N + 1)]

    low = 0
    high = L

    while(True):
        if(high - low == 1):
            print(low)
            break

        x = (high + low) // 2
        now = 0
        count = 0
        for length in lengths:
            now += length
            if(now >= x):
                now = 0
                count += 1

        if(count >= K + 1):  # success
            low = x
        else:
            high = x


if(__name__ == "__main__"):
    main()
