MOD = 1000000007


def main():
    H, W = map(int, input().split())
    C = []
    for _ in range(H):
        s = input()
        c = 0
        for i in range(W):
            c += 0 if s[i] == "." else (1 << i)
        C.append(c)

    BIT = pow(2, W)
    dp = [[None] * BIT for _ in range(H)]

    def func(h, last_bit):
        if(h == H):
            return 1

        count = 0
        for bit in range(BIT):
            if(bit & C[h] == 0):
                if(bit & (last_bit << 1) == 0 and bit & last_bit == 0 and bit & (last_bit >> 1) == 0):
                    if(bit & (bit << 1) == 0 and bit & (bit >> 1) == 0):
                        if(dp[h][bit] is not None):
                            count += dp[h][bit]
                            count %= MOD
                        else:
                            dp[h][bit] = func(h + 1, bit)
                            count += dp[h][bit]
                            count %= MOD

        return count

    print(func(0, 0))


if(__name__ == "__main__"):
    main()
