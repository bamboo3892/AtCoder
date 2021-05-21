import math


def main():
    a = int(input())
    for i in range(int(math.sqrt(a)) + 1, 0, -1):
        if(a % i == 0):
            print(int(i + (a / i) - 2))
            return


if(__name__ == "__main__"):
    main()
