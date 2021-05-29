

def main():
    N, M = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]

    ans = 0
    for m1 in range(M - 1):
        for m2 in range(m1 + 1, M):
            ans += LR[m1][0] < LR[m2][0] < LR[m1][1] < LR[m2][1] or LR[m2][0] < LR[m1][0] < LR[m2][1] < LR[m1][1]
    print(ans)


if(__name__ == "__main__"):
    main()
