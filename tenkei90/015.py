MOD = 1000000007

N = 10 ** 5
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)


def main():
    N = int(input())

    for k in range(1, N + 1):
        ans = 0
        n = 1
        while(cmb(N - (k - 1) * (n - 1), n) != 0):
            ans += cmb(N - (k - 1) * (n - 1), n)
            n = n + 1
        print(ans % MOD)


def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % MOD



if(__name__ == "__main__"):
    main()
