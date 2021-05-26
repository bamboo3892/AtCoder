

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    sum_ = 0
    for i in range(N):
        sum_ += abs(A[i] - B[i])

    print(sum_)


if(__name__ == "__main__"):
    main()
