

def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    # answer will be in (lower, upper]
    lower = 0
    upper = pow(10, 9)
    while(True):
        now = (upper + lower) // 2
        f = func(A, now, N, K)

        if(f):
            upper = now
        else:
            lower = now

        if(upper - lower == 1):
            print(lower if func(A, lower, N, K) else upper)
            break


def func(A, now, N, K):
    t = [[0] * (N + 1) for _ in range(N + 1)]
    for n1 in range(1, N + 1):
        for n2 in range(1, N + 1):
            t[n1][n2] = t[n1][n2 - 1] + t[n1 - 1][n2] - t[n1 - 1][n2 - 1] + (A[n1 - 1][n2 - 1] > now)

    for n1 in range(N - K + 1):
        for n2 in range(N - K + 1):
            sum_ = t[n1 + K][n2 + K] - t[n1][n2 + K] - t[n1 + K][n2] + t[n1][n2]
            if(sum_ <= (K ** 2) // 2):
                return True

    return False


if(__name__ == "__main__"):
    main()
