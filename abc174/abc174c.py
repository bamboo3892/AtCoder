K = int(input())

if(K in [1, 7]):
    print(1)
else:
    now = 7 % K
    a = 10 % K
    for n in range(2, 1000001):
        now = (now * a + 7) % K
        if(now == 0):
            print(n)
            break
    else:
        print(-1)
