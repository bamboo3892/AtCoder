import math
import numpy as np
import bisect


def main():
    N = int(input())
    S = input()
    T = input()

    i0 = []
    i1 = []
    pair = []
    total0 = [0] * N
    nowTotal = 0
    for n in range(N):
        if(S[n] != T[n]):
            if(S[n] == "0"):
                if(len(i1) != 0):
                    pair.append([i1.pop(0), n])
                else:
                    i0.append(n)
            else:
                if(len(i0) != 0):
                    pair.append([i0.pop(0), n])
                else:
                    i1.append(n)

        if(S[n] == "0"):
            nowTotal += 1
        total0[n] = nowTotal

    if(len(i0) != 0 or len(i1) != 0):
        print("-1")
        return

    ans = 0
    opened = False
    close = []
    for n in range(N):
        if(len(pair) != 0 and pair[0][0] == n):
            opened = True
            bisect.insort(close, pair[0][1])
            pair.pop(0)

        if(S[n] == "0" and opened):
            ans += 1

        while(len(close) != 0 and n == close[0]):
            close.pop(0)
        opened = len(close) != 0
    print(ans)


if(__name__ == "__main__"):
    main()
