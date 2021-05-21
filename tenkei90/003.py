import math
import numpy as np


def main():
    N = int(input())
    graph = [[] for _ in range(N)]
    for n in range(N - 1):
        x = [int(a) for a in input().split(" ")]
        graph[x[0] - 1].append(x[1] - 1)
        graph[x[1] - 1].append(x[0] - 1)

    x, _ = getFarthestNode(graph, 0, N)
    y, length = getFarthestNode(graph, x, N)

    print(length + 1)


def getFarthestNode(g, start, N):
    dist = [-1] * N
    dist[start] = 0
    q = [start]
    count = 1

    while True:
        u = q.pop()
        for v in g[u]:
            if dist[v] != -1:
                continue
            count += 1
            dist[v] = dist[u] + 1
            q.append(v)
        if count >= N:
            break
    node = np.argmax(dist)
    return node, dist[node]


# def getFarthestNode(graph, start, N):
#     x = [-1] * N  # distance from x
#     x[start] = 0

#     func(graph, x, start)

#     node = np.argmax(x)
#     return node, x[node]


# def func(graph, x, node):
#     for n in graph[node]:
#         if(x[n] == -1):
#             x[n] = x[node] + 1
#             func(graph, x, n)


if(__name__ == "__main__"):
    main()
