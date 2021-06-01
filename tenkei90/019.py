

def main():
    N = int(input())
    A = list(map(int, input().split()))

    dp = [[0] * (2 * N + 1) for _ in range(2 * N + 1)]

    for num in range(2, 2 * N + 2, 2):
        for i1 in range(0, 2 * N - num + 1):
            i2 = i1 + num

            # update dp[i1][i2]
            min_ = dp[i1 + 1][i2 - 1] + abs(A[i1] - A[i2 - 1])
            for k in range(2, num, 2):
                min_ = min([min_, dp[i1][i1 + k] + dp[i1 + k][i2]])
            dp[i1][i2] = min_
    print(dp[0][2 * N])


if(__name__ == "__main__"):
    main()
