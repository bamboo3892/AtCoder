
def main():
    x = [int(a) for a in input().split(" ")]
    N = x[0]
    P = x[1]
    # a = (P - 1) * ((P - 2) ** (N - 1))
    a = (P - 1) * pow(P - 2, N - 1, 10 ** 9 + 7)
    a %= 10 ** 9 + 7
    print(a)


if(__name__ == "__main__"):
    main()
