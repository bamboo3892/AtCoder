import numpy as np


def main():
    N = int(input())
    d = np.array([int(a) for a in input().split(" ")])
    s = np.sum(d)
    s2 = np.sum(d * d)
    print(int((s * s - s2) / 2))


if(__name__ == "__main__"):
    main()
