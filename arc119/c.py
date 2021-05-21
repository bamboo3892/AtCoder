import math
import numpy as np
import bisect


def main():
    N = int(input())
    A = list(map(int, input().split()))

    sum_ = [0]
    for n in range(N):
        sum_.append(sum_[-1] + A[n] * (1 if n % 2 == 1 else -1))
    sum_.sort()

    ans = 0
    last = sum_[0]
    num = 1
    for s in sum_[1:]:
        if(last == s):
            num += 1
        else:
            ans += (num - 1) * num // 2
            last = s
            num = 1
    ans += (num - 1) * num // 2

    print(ans)


if(__name__ == "__main__"):
    main()
