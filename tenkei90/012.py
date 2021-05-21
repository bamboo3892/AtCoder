import math
import sys
sys.setrecursionlimit(int(1e7))


def main():
    H, W = map(int, input().split())
    Q = int(input())
    q = [list(map(int, input().split())) for _ in range(Q)]

    table = [[0] * (W + 2) for _ in range(H + 2)]
    OFFSET = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 上下左右

    uf = UnionFind(Q)
    new_groupID = 1
    for query in q:
        if(query[0] == 1):
            table[query[1]][query[2]] = new_groupID
            for dx, dy in OFFSET:
                if(table[query[1] + dx][query[2] + dy] != 0):
                    uf.union(new_groupID, table[query[1] + dx][query[2] + dy])
            new_groupID += 1
        else:
            if(table[query[1]][query[2]] == 0 or table[query[3]][query[4]] == 0):
                print("No")
                continue
            id1 = uf.find(table[query[1]][query[2]])
            id2 = uf.find(table[query[3]][query[4]])
            print("Yes" if id1 == id2 else "No")


class UnionFind(object):

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]
        self.n = n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]


if(__name__ == "__main__"):
    main()
