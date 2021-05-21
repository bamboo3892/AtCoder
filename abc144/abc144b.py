
def main():
    a = int(input())
    for i in range(1, 10):
        if(a % i == 0 and a / i < 10):
            print("Yes")
            return
    print("No")


if(__name__ == "__main__"):
    main()
