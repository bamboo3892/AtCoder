import math
import numpy as np


def main():
    N = int(input())
    B = int(math.log(N, 2)) + 1

    ans = N  # b == 0
    for k in range(1, B):
        a = N // pow(2, k)
        abc = a + k + (N - a * pow(2, k))
        ans = min([ans, abc])
    print(ans)


if(__name__ == "__main__"):
    main()
