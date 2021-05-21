s = [int(a) for a in input().split(" ")]
N = s[0]
D2 = s[1] ** 2

count = 0
for i in range(N):
    s = [int(a) for a in input().split(" ")]
    dis2 = s[0] ** 2 + s[1] ** 2
    if(dis2 <= D2):
        count += 1

print(count)
