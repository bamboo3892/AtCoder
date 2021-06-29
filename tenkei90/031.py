import math


def main():
    N = int(input())
    W = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0
    for n in range(N):
        ans ^= calc_grundy(W[n], B[n])

    print("Second" if ans == 0 else "First")


grundy = [[None] * 1326 for _ in range(51)]  # 0:必敗, 1以上:必勝


def calc_grundy(w, b):
    if(grundy[w][b] is not None):
        return grundy[w][b]
    else:
        if(w == 0 and b in [0, 1]):
            grundy[w][b] = 0
        else:
            g = set()
            if(w != 0):
                g.add(calc_grundy(w - 1, b + w))
            for sub_b in range(1, b // 2 + 1):
                g.add(calc_grundy(w, b - sub_b))
            grundy[w][b] = mex(g)
        return grundy[w][b]


def mex(s):
    l = [-1] + sorted(list(s))
    for i in range(len(l) - 1):
        if(l[i] + 1 != l[i + 1]):
            return l[i] + 1
    return l[-1] + 1


if(__name__ == "__main__"):
    main()
