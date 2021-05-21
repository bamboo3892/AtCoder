import math
import numpy as np


def main():
    N, B, K = map(int, input().split())
    C = list(map(int, input().split()))

    MOD = pow(10, 9) + 7

    dp = np.zeros((N, B), dtype=int)
    for c in C:
        dp[0, c % B] += 1

    for n in range(1, N):  # n+1桁
        for b in range(B):
            for c in C:
                rest = (10 * b + c) % B
                dp[n, rest] += dp[n - 1, b]
                dp[n, rest] %= MOD

    print(dp[-1, 0])


if(__name__ == "__main__"):
    main()
