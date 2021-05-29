import math


def main():
    T = int(input())
    L, X, Y = map(int, input().split())
    Q = int(input())
    E = [int(input()) for _ in range(Q)]

    for e in E:
        cos = math.cos(2 * math.pi * e / T)
        sin = math.sin(2 * math.pi * e / T)
        den = math.sqrt(pow(X, 2) + pow(Y + L / 2 * sin, 2))
        ans = abs(math.atan2(L / 2 * (1 - cos), den)) * 180 / math.pi
        print(ans)


if(__name__ == "__main__"):
    main()
