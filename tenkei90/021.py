

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(a)]

    graph = [[] for _ in range(N)]
    for _ in range(M):
        ab = [int(a) for a in input().split()]
        graph[ab[0] - 1].append(ab[1])

    now = 0
    t = [None] * N
    while(True):
        pass


if(__name__ == "__main__"):
    main()
