import math
import numpy as np


def main():
    N = int(input())
    c = list(input())

    # now = c[0]
    # for i in range(1, N):
    #     if(c[i] == now):
    #         continue
    #     else:
    #         if(c[i] == "B"):
    #             if(now == "W"):
    #                 now = "R"
    #             else:
    #                 now = "W"

    #         elif(c[i] == "W"):
    #             if(now == "R"):
    #                 now = "B"
    #             else:
    #                 now = "R"

    #         else:
    #             if(now == "B"):
    #                 now = "W"
    #             else:
    #                 now = "B"

    # print(now)

    x = np.zeros((N, 3), dtype="i1")
    x[c == "B", 0] = 1
    x[c == "W", 1] = 1
    x[c == "R", 2] = 1

    for i in range(N - 1):
        tmp = np.zeros((x.shape[0] - 1, 3), dtype="i1")
        tmp[:, 0] = x[0:-1, 1] * x[1:, 2] - x[0:-1, 2] * x[1:, 1]
        tmp[:, 1] = x[0:-1, 2] * x[1:, 0] - x[0:-1, 0] * x[1:, 2]
        tmp[:, 2] = x[0:-1, 0] * x[1:, 1] - x[0:-1, 1] * x[1:, 0]
        f = tmp.sum(axis=1) == 0
        tmp[f] = x[0:-1][f]
        x = tmp

    if(x[0, 0] != 0):
        print("B")
    elif(x[0, 1] != 0):
        print("W")
    else:
        print("R")


if(__name__ == "__main__"):
    main()
