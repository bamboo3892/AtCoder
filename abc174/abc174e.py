import math

s = [int(a) for a in input().split(" ")]
N = s[0]
K = s[1]
As = [int(a) for a in input().split(" ")]
As = sorted(As)[::-1]


def func(minimun):
    count = 0
    for A in As:
        if(A > minimun):
            count += A // minimun
            if(count > K):
                return False
        else:
            return True
    return True


bound = [0, As[0]]
while(True):
    i = (bound[0] + bound[1]) / 2
    if(func(i)):
        bound[1] = i
    else:
        bound[0] = i

    if(bound[1] - bound[0] <= 0.001):
        print(math.ceil(bound[0]))
        break
