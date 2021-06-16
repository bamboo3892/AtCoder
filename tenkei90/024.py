

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dif = 0
    for n in range(N):
        dif += abs(A[n] - B[n])

    if(K < dif):
        print("No")
    else:
        if(K & 1 == dif & 1):
            print("Yes")
        else:
            print("No")


if(__name__ == "__main__"):
    main()
