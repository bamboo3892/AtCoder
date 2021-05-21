import math
import numpy as np


def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    A = np.array(A)

    h = A.sum(axis=1)
    w = A.sum(axis=0)

    B = h[:, None] + w[None, :] - A

    for b in B:
        print(" ".join(map(str, b.tolist())))


if(__name__ == "__main__"):
    main()
