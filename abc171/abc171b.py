import numpy as np

s = input().split(" ")
p = input().split(" ")
N = int(s[0])
K = int(s[1])
p = np.array([int(p[n]) for n in range(N)])
print(np.sum(np.sort(p)[0:K]))
