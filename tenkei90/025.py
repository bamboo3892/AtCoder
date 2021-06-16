

def main():
    N, B = map(int, input().split())
    a = len(str(N))

    def func(lis, nex, f):
        count = 0
        m = f + B
        if(m <= N):
            m = list(map(int, list(str(m))))
            if(len(m) == len(lis)):
                for n in range(len(lis)):
                    if(lis[n] in m):
                        m.remove(lis[n])
                    else:
                        break
                else:
                    count += 1

        if(len(lis) == a):
            return count

        for i in range(nex, 10):
            count += func(lis + [i], i, f * i)

        return count

    print(func([], 0, 1))


if(__name__ == "__main__"):
    main()
