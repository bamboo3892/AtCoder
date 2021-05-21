import math
import numpy as np


def main():
    N = int(input())
    A = [int(a) for a in input().split(" ")]

    state = np.zeros((200), dtype=int)  # 0: 到達不可, 1:+のみ, 2:-のみ, 3:+のみか-のみ, 4:到達可能
    table = np.zeros((200, N), dtype=int)
    table2 = np.zeros((200, N), dtype=int)  # 予備
    state_tmp = state.copy()
    table_tmp = table.copy()
    table2_tmp = table2.copy()

    def func1(n, rest, sign):  # table[rest]をどう編集するか
        s = 1 if sign == 1 else 2
        if(state[rest] == 0):
            state_tmp[rest] = s
            table_tmp[rest, n] = sign
        elif((state[rest] == 1 and s == 2) or (state[rest] == 2 and s == 1)):
            state_tmp[rest] = 3
            table2_tmp[rest, n] = sign


    def func2(n, rest, sign, i):  # table[rest + i]をどう編集するか
        r = (rest + i) % 200

        if(state[i] == 4):  # -> 4
            state_tmp[r] = 4
        elif(state[i] == 3):  # -> 4
            state_tmp[r] = 4
            if((table[rest] == 1).any() ^ (sign == 1)):
                table_tmp[r] = table[rest]
                table_tmp[r, n] = sign
            else:
                table_tmp[r] = table2[rest]
                table_tmp[r, n] = sign

        elif((state[i] == 1) ^ (sign == 1)):  # -> 3
            state_tmp[r] = 3
            table2_tmp[r, n] = sign

        else:  # -> 1 or 2
            state_tmp[r] = 1 if sign == 1 else 2
            table_tmp[r, n] = sign


    for n in range(N):
        rest1 = A[n] % 200
        rest2 = (-A[n]) % 200

        func1(n, rest1, 1)
        func1(n, rest2, -1)
        for i in range(200):
            if(state[i] != 0):
                func2(n, rest1, 1, i)
                func2(n, rest2, -1, i)

        state = state_tmp.copy()
        table = table_tmp.copy()
        table2 = table2_tmp.copy()


    if(state[0] == 4):
        l1 = []
        l2 = []
        for n in range(N):
            if(table[0, n] == 1):
                l1.append(str(n + 1))
            elif(table[0, n] == -1):
                l2.append(str(n + 1))
        print("Yes")
        print(str(len(l1)) + " " + " ".join(l1))
        print(str(len(l2)) + " " + " ".join(l2))
    else:
        print("No")


if(__name__ == "__main__"):
    main()
