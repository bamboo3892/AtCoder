
def main():
    x = [int(a) for a in input().split(" ")]
    N = x[0]
    M = x[1]
    A = [int(a) for a in input().split(" ")]
    B = [int(a) for a in input().split(" ")]

    common = set(A) ^ set(B)
    common = sorted(list(common))
    print(" ".join(str(a) for a in common))


if(__name__ == "__main__"):
    main()
