import numpy as np


def main():
    N = int(input())
    lr = [list(map(int, input().split())) for _ in range(N)]

    table = np.zeros((1005, 1005), dtype=int)
    for lx, ly, rx, ry in lr:
        table[lx, ly] += 1
        table[lx, ry] -= 1
        table[rx, ly] -= 1
        table[rx, ry] += 1

    for i in range(1004):
        table[i + 1] += table[i]
    for i in range(1004):
        table[:, i + 1] += table[:, i]

    l = [0] * (N + 1)
    for x in range(1005):
        for y in range(1005):
            l[table[x, y]] += 1

    for k in range(1, N + 1):
        print(l[k])


if(__name__ == "__main__"):
    main()
