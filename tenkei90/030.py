

def main():
    N, K = map(int, input().split())

    t = [0] * (N + 1)
    for n in range(2, N + 1):
        if(t[n] == 0):
            for k in range(n, N + 1, n):
                t[k] += 1

    ans = 0
    for n in range(2, N + 1):
        if(t[n] >= K):
            ans += 1
    print(ans)


if(__name__ == "__main__"):
    main()
