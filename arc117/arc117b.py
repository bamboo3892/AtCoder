import math
import numpy as np


MOD = pow(10, 9) + 7


def main():
    N = int(input())
    A = np.array([int(a) for a in input().split(" ")], dtype=np.int64)
    A = np.sort(A)[::-1]
    result = 1
    for i in range(N - 1):
        result *= (A[i] - A[i + 1] + 1)
        result %= MOD
    result *= (A[N - 1] + 1)
    result %= MOD
    print(result)


if(__name__ == "__main__"):
    main()
