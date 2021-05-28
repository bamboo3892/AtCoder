

def main():
    N = int(input())
    ABC = list(map(int, input().split()))

    ABC = sorted(ABC)[::-1]

    ans = pow(10, 6)
    for a in range(N // ABC[0], -1, -1):
        rest1 = N - ABC[0] * a
        for b in range(rest1 // ABC[1], -1, -1):
            rest2 = rest1 - ABC[1] * b
            if(rest2 % ABC[2] == 0):
                ans = min([ans, a + b + rest2 // ABC[2]])

    print(ans)


if(__name__ == "__main__"):
    main()
