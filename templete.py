import math
import numpy as np

import sys
sys.setrecursionlimit(int(1e7))

MOD = 1000000007


def main():
    x = int(input())
    N, M = map(int, input().split())
    x = list(map(int, input().split()))
    x = [int(input()) for _ in range(N)]
    x = [list(map(int, input().split())) for _ in range(N)]

    graph = [[] for _ in range(N)]
    for _ in range(M):
        abc = [int(a) for a in input().split()]
        graph[abc[0] - 1].append([abc[1] - 1, abc[2]])
        graph[abc[1] - 1].append([abc[0] - 1, abc[2]])

    for _ in range(M):
        abc = [int(a) for a in input().split()]
        graph[abc[0] - 1].append(abc[1] - 1)
        graph[abc[1] - 1].append(abc[0] - 1)


if(__name__ == "__main__"):
    main()
