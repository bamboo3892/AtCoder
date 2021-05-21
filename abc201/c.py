import math
import numpy as np


def main():
    S = input()

    result = 0
    for i in range(10000):
        num = "{:04}".format(i)
        flag = [S[n] != "o" for n in range(10)]
        flag2 = True
        for n in num:
            n = int(n)
            if(S[n] == "o"):
                flag[n] = True
            elif(S[n] == "x"):
                flag2 = False
                break
        if(np.all(flag) and flag2):
            result += 1
    print(result)


if(__name__ == "__main__"):
    main()
