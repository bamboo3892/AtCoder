

def main():
    N, K = map(int, input().split())

    a = int(str(K * N * (N + 1) // 2) + "00")
    a += N * K * (K + 1) // 2
    print(a)


if(__name__ == "__main__"):
    main()
