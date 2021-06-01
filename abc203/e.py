

def main():
    N, M = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(M)]

    XY.sort(key=lambda xy: xy[0])

    bound = [N, N]
    next_bound = [N, N]
    last_x = 0
    for x, y in XY:
        if(last_x != x):
            bound = next_bound.copy()

        if(y == bound[0] == bound[1]):
            if(next_bound[0] == next_bound[1] == y):
                print(0)
                exit()
            elif(next_bound[0] == y):
                next_bound[0] += 1
            elif(next_bound[1] == y):
                next_bound[1] -= 1
        if(y == bound[0] - 1):
            next_bound[0] = bound[0] - 1
        elif(y == bound[1] + 1):
            next_bound[1] = bound[1] + 1
        last_x = x

    bound = next_bound.copy()

    print(bound[1] - bound[0] + 1)


if(__name__ == "__main__"):
    main()
