import sys
sys.setrecursionlimit(int(1e7))


def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    graph_r = [[] for _ in range(N)]
    for _ in range(M):
        ab = [int(a) for a in input().split()]
        graph[ab[0] - 1].append(ab[1] - 1)
        graph_r[ab[1] - 1].append(ab[0] - 1)

    label, group = scc(N, graph, graph_r)
    label, group = construct(N, graph, label, group)

    ans = 0
    for g in group:
        ans += len(g) * (len(g) - 1) // 2
    print(ans)


def scc(N, G, RG):

    order = []
    used = [0] * N
    group = [None] * N

    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)

    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)
    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0] * N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group


def construct(N, G, label, group):
    G0 = [set() for i in range(label)]
    GP = [[] for i in range(label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v)
    return G0, GP


if(__name__ == "__main__"):
    main()
