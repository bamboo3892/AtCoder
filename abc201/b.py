import math
import numpy as np


def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    arg = np.argsort(T)

    print(S[arg[-2]])


if(__name__ == "__main__"):
    main()
