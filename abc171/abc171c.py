import numpy as np

CHAR = "abcdefghijklmnopqrstuvwxyz"

N = int(input()) - 1
s = ""

while(True):
    b = N % 26
    N = N // 26
    s = CHAR[b] + s
    if(N == 0):
        print(s)
        break
    N -= 1
