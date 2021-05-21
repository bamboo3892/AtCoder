import math


def main():
    x = [int(a) for a in input().split(" ")]
    y = x[1] / x[0] * x[2]
    if(y % 1 == 0):
        y = int(y) - 1
    else:
        y = int(y)
    print(y)


if(__name__ == "__main__"):
    main()
