import math
import numpy as np


def main():
    N, K = map(int, input().split())
    S = input()
    s = [ord(c) - 97 for c in S]

    dp = np.full((N, 26), N + 100)
    a = np.full(26, N + 100)
    for n in range(N - 1, -1, -1):
        a[s[n]] = n
        dp[n] = a

    s2 = []
    now = 0
    for k in range(K):
        rest = K - k
        for c in range(26):
            if(dp[now, c] <= N - rest):
                s2.append(c)
                now = dp[now, c] + 1
                break

    print(func(s2))


def func(s):
    s2 = []
    for c in s:
        if(c != -1):
            s2.append(c)
    return "".join([chr(c + 97) for c in s2])


if(__name__ == "__main__"):
    main()
