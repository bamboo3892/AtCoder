import numpy as np

N = int(input())
a = np.fromstring(input(), sep=" ", dtype=np.int64)
b = np.bitwise_xor.reduce(a)
c = np.bitwise_xor(a, b)
print(*c, sep=" ")
