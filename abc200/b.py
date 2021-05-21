import math
import numpy as np


def main():
    x = [int(a) for a in input().split(" ")]
    N = x[0]
    K = x[1]

    for k in range(K):
        if(N % 200 == 0):
            N = N // 200
        else:
            N = int(str(N) + "200")
    print(N)


if(__name__ == "__main__"):
    main()
