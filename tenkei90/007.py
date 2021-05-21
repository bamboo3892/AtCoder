import math
import numpy as np
import bisect


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = np.sort(A).tolist()
    Q = int(input())
    B = [int(input()) for _ in range(Q)]

    for b in B:
        i = bisect.bisect(A, b)
        if(i == 0):
            nnn = abs(A[i] - b)
        elif(i == N):
            nnn = abs(A[i - 1] - b)
        else:
            nnn = min([abs(A[i - 1] - b), abs(A[i] - b)])
        print(nnn)


if(__name__ == "__main__"):
    main()
