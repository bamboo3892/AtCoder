import numpy as np


def main():
    N = int(input())
    A = np.fromstring(input(), sep=" ", dtype=np.int64)
    Q = int(input())
    B = np.zeros(Q)
    C = np.zeros(Q)
    D = np.fromstring(" ".join([input() for q in range(Q)]), sep=" ", dtype=np.int64).reshape((Q, 2))
    B = D[:, 0]
    C = D[:, 1]

    d = dict(np.c_[np.unique(A, return_counts=True)])
    s = np.sum(A)
    for q in range(Q):
        if(B[q] in d):
            n = d.pop(B[q])
            s += n * (C[q] - B[q])
            if(C[q] in d):
                d[C[q]] += n
            else:
                d[C[q]] = n
        print(s)


main()
