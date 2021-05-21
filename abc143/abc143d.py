import numpy as np
import math


def main():
    N = int(input())
    L = np.array([int(a) for a in input().split(" ")])
    L.sort()
    count = 0
    for n1 in range(1, N - 2):
        for n2 in range(n1 + 1, N - 1):
            s = L[n1] + L[n2]
            # m = abs(L[n1] - L[n2])
            L2 = L[n2 + 1:]
            count += np.sum(L2 < s)
            # count += np.sum(np.logical_and(L2 < s, L2 > m))
    print(count)


if(__name__ == "__main__"):
    main()
