import math
import numpy as np


def main():
    x = [int(a) for a in input().split(" ")]
    A = x[0]
    B = x[1]

    l = []
    if(B > A):
        l += np.arange(-1, -B - 1, -1).tolist()
        l += np.arange(1, A).tolist()
        l += [int(B * (B + 1) / 2 - (A - 1) * A / 2)]
    elif(A > B):
        l += np.arange(1, A + 1).tolist()
        l += np.arange(-1, -B, -1).tolist()
        l += [int(- A * (A + 1) / 2 + (B - 1) * B / 2)]
    else:
        l += np.arange(1, A + 1).tolist()
        l += np.arange(-1, -B - 1, -1).tolist()

    print(" ".join([str(a) for a in l]))


if(__name__ == "__main__"):
    main()
