import bisect


def main():
    N = int(input())
    S = [input() for _ in range(N)]

    # lis = []
    # ans = []
    # for n in range(N):
    #     s = S[n]
    #     i = bisect.bisect_left(lis, s)
    #     if(i == len(lis) or lis[i] != s):
    #         lis.insert(i, s)
    #         ans.append(str(n + 1))

    set_ = set()
    ans = []
    for n in range(N):
        s = S[n]
        if(s not in set_):
            set_.add(s)
            ans.append(str(n + 1))

    print("\n".join(ans))


if(__name__ == "__main__"):
    main()
