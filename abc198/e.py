import math
import numpy as np


def main():
    N = int(input())
    C = [int(a) for a in input().split(" ")]
    A = [0] * (N-1)
    B = [0] * (N-1)
    for i in range(N-1):
        x = [int(a) for a in input().split(" ")]
        A[i] = x[0]
        B[i] = x[1]

    sortedA = np.argsort(A)
    sortedB = np.argsort(B)





if(__name__ == "__main__"):
    main()
