import sys
sys.setrecursionlimit(int(1e7))


def main():
    N = int(input())
    N2 = N // 2

    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        abc = [int(a) for a in input().split()]
        graph[abc[0] - 1].append(abc[1] - 1)
        graph[abc[1] - 1].append(abc[0] - 1)

    # groups = [[], []]
    # added = [False] * N

    # def dfs(start, gid):
    #     added[start] = True
    #     groups[gid].append(start)
    #     for i in graph[start]:
    #         if(not added[i]):
    #             dfs(i, gid ^ 1)

    # dfs(0, 0)

    groups = [[], []]
    added = [False] * N
    next_search = [0]
    next_gid = 0

    while(len(next_search)):
        tmp = []
        for i in next_search:
            groups[next_gid].append(i)
            added[i] = True
            for i2 in graph[i]:
                if(not added[i2]):
                    tmp.append(i2)
        next_search = tmp
        next_gid ^= 1

    if(len(groups[0]) >= N2):
        print(" ".join([str(a + 1) for a in groups[0][:N2]]))
    else:
        print(" ".join([str(a + 1) for a in groups[1][:N2]]))


if(__name__ == "__main__"):
    main()
