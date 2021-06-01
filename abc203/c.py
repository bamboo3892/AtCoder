

def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    AB.sort(key=lambda ab: ab[0])

    now = 0
    rest = K
    for ab in AB:
        if(ab[0] > now + rest):
            print(now + rest)
            exit()
        rest += ab[1] - (ab[0] - now)
        now = ab[0]
    print(now + rest)


if(__name__ == "__main__"):
    main()
