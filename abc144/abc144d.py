import math


def main():
    s = input().split(" ")
    a = float(s[0])
    b = float(s[1])
    x = float(s[2])
    if(a * a * b / 2 < x):
        print(math.atan(2 * (a * a * b - x) / a / a / a) / math.pi * 180)
    else:
        print(math.atan(a * b * b / 2 / x) / math.pi * 180)


if(__name__ == "__main__"):
    main()
