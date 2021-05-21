import math
import numpy as np


def main():
    N = int(input())
    S = input()
    MOD = 1000000007
    STR = "atcoder"

    t = np.zeros((N, len(STR)), dtype=np.int64)
    nnn = 0
    for n in range(N):
        if(S[n] == STR[0]):
            nnn += 1
        t[n, 0] = nnn

    for n in range(1, N):
        for i in range(1, len(STR)):
            if(i > n):
                continue
            if(S[n] == STR[i]):
                t[n, i] = (t[n - 1, i] + t[n, i - 1]) % MOD
            else:
                t[n, i] = t[n - 1, i]
    print(t[N - 1, 6])


if(__name__ == "__main__"):
    main()
