import numpy as np


def main():
    N = int(input())
    S = input()
    count = 1
    now = S[0]
    for n in range(1, N):
        if(now != S[n]):
            count += 1
            now = S[n]
    print(count)


if(__name__ == "__main__"):
    main()
