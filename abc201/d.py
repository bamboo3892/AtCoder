import math


def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]

    # H = W = 2000
    # A = ["+" * W for _ in range(H)]

    dp = [[0] * W for _ in range(H)]
    for h in range(H - 1, -1, -1):
        for w in range(W - 1, -1, -1):
            """
            (h,w)からスタートしたとき高橋くんは最善で何点勝っているか
            """
            teban = (h + w) % 2 == 0
            if(h == H - 1 and w == W - 1):
                dp[h][w] = 0
            elif(h == H - 1):
                dp[h][w] = dp[h][w + 1] + (2 if A[h][w + 1] == "+" else -2) * (1 if teban else -1)
            elif(w == W - 1):
                dp[h][w] = dp[h + 1][w] + (2 if A[h + 1][w] == "+" else -2) * (1 if teban else -1)
            else:
                n1 = dp[h][w + 1] + (2 if A[h][w + 1] == "+" else -2) * (1 if teban else -1)
                n2 = dp[h + 1][w] + (2 if A[h + 1][w] == "+" else -2) * (1 if teban else -1)
                dp[h][w] = (max([n1, n2]) if teban else min([n1, n2]))

    result = dp[0][0]
    print("Takahashi" if result > 0 else "Aoki " if result < 0 else "Draw")


if(__name__ == "__main__"):
    main()
