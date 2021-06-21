import numpy as np


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = np.array(A)
    A, counts = np.unique(A, return_counts=True)

    ans = 0
    sum_ = 0
    for c in counts:
        ans += sum_ * c
        sum_ += c

    print(ans)


if(__name__ == "__main__"):
    main()
