import math
import numpy as np


def main():
    x = [int(a) for a in input().split(" ")]
    R = x[0]
    X = x[1]
    Y = x[2]

    x = (X ** 2 + Y ** 2) / R ** 2
    x = math.ceil(x)
    x = math.ceil(math.sqrt(x))

    if(x == 1):
        if((X ** 2 + Y ** 2) == R ** 2):
            print(1)
        else:
            print(2)
    else:
        print(x)


if(__name__ == "__main__"):
    main()
