import math
import numpy as np


def main():
    N = input()

    n = 0
    for i in range(len(N)):
        if(N[i] == "0"):
            n += 1
    N = N[:len(N) - n]

    n = 0
    for i in range(len(N)):
        if(N[len(N) - i - 1] == "0"):
            n += 1
    N = N[n:]

    if(N == ""):
        print("Yes")
    else:
        for i in range(len(N)):
            if(N[i] != N[len(N) - i - 1]):
                print("No")
                return
        print("Yes")


if(__name__ == "__main__"):
    main()
