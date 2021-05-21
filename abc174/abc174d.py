N = int(input())
c = input()

r_count = 0
for i in range(N):
    if(c[i] == "R"):
        r_count += 1
w = 0
for i in range(r_count):
    if(c[i] == "W"):
        w += 1

print(w)
