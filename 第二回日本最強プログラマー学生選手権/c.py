import math


def main():
    x = [int(a) for a in input().split(" ")]
    A = x[0]
    B = x[1]
    max_gcd = 1

    for gcd in range(2, int(B / 2) + 1):
        a = math.ceil(A / gcd)
        b = int(B / gcd)
        if((b - a) >= 1):
            max_gcd = gcd

    print(max_gcd)


if(__name__ == "__main__"):
    main()
