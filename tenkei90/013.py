from heapq import heappush, heappop


def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        abc = [int(a) for a in input().split(" ")]
        graph[abc[0] - 1].append([abc[1] - 1, abc[2]])
        graph[abc[1] - 1].append([abc[0] - 1, abc[2]])

    lengths1 = dijkstra(graph, 0)
    lengths2 = dijkstra(graph, N - 1)

    for k in range(N):
        print(lengths1[k] + lengths2[k])


def dijkstra(graph, start):
    lengths = [float("inf")] * len(graph)
    lengths[start] = 0
    fixed = [False] * len(graph)
    heap = [(0, start)]

    while(heap):
        a = heappop(heap)[1]
        if(fixed[a]):
            continue
        fixed[a] = True

        for b, c in graph[a]:
            if(not fixed[b] and lengths[a] + c < lengths[b]):
                lengths[b] = lengths[a] + c
                heappush(heap, (lengths[b], b))
    return lengths


if(__name__ == "__main__"):
    main()
