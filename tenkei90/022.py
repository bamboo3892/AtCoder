import math


def main():
    A, B, C = map(int, input().split())
    gcd = math.gcd(A, B)
    gcd = math.gcd(gcd, C)

    ans = 0
    ans += A // gcd - 1
    ans += B // gcd - 1
    ans += C // gcd - 1
    print(ans)


if(__name__ == "__main__"):
    main()
