import math
import bisect
import random


def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    # N = 2000
    # nnn = pow(10, 9)
    # XY = [[random.randint(0, nnn), random.randint(0, nnn)] for _ in range(N)]

    max_angle = -100
    for n1 in range(N):
        angle = [None] * N
        for n2 in range(N):
            if(n1 == n2):
                continue
            dx = XY[n2][0] - XY[n1][0]
            dy = XY[n2][1] - XY[n1][1]
            r = math.sqrt(pow(dx, 2) + pow(dy, 2))
            a = math.degrees(math.acos(dx / r))
            angle[n2] = a if dy >= 0 else 360 - a

        angle_s = angle.copy()
        angle_s.pop(n1)
        angle_s = sorted(angle_s)

        for n2 in range(N):
            if(n1 == n2 or len(angle_s) == 1):
                continue
            angle_s.remove(angle[n2])  # n2を使う組み合わせはこれ以降探索しなくていいので消しちゃう
            tmp_angle = [angle_s[-1] - 360] + angle_s + [angle_s[0] + 360]

            a = (angle[n2] + 180) % 360
            i = bisect.bisect(tmp_angle, a)

            min_ = min([abs(tmp_angle[i - 1] - a), abs(tmp_angle[i] - a)])
            max_angle = max([180 - min_, max_angle])

    print(max_angle)


if(__name__ == "__main__"):
    main()
