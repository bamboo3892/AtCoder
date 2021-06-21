import math


def main():
    N = int(input())
    W = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0
    for n in range(N):
        ans += W[n]
        b2 = B[n] + W[n] * (W[n] + 1) // 2
        if(b2 >= 2):
            ans += int(math.log(b2 - 1, 2)) + 1

    print("First" if ans % 2 else "Second")


if(__name__ == "__main__"):
    main()
