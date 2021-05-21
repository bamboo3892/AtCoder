import math
import numpy as np


def main():
    N = int(input())
    CP = [list(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    LR = [list(map(int, input().split())) for _ in range(Q)]

    sum1 = [0]
    sum2 = [0]
    for n in range(N):
        if(CP[n][0] == 1):
            sum1.append(sum1[-1] + CP[n][1])
            sum2.append(sum2[-1])
        else:
            sum1.append(sum1[-1])
            sum2.append(sum2[-1] + CP[n][1])

    for q in range(Q):
        a = sum1[LR[q][1]] - sum1[LR[q][0] - 1]
        b = sum2[LR[q][1]] - sum2[LR[q][0] - 1]
        print(f"{a} {b}")


if(__name__ == "__main__"):
    main()
