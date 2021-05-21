

def main():
    H, W = map(int, input().split())
    r_s, c_s = map(lambda x: int(x) - 1, input().split())
    r_t, c_t = map(lambda x: int(x) - 1, input().split())
    S = [input() for _ in range(H)]
    OFFSET = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 上下左右

    # H, W = 1000, 1000
    # r_s, c_s = 0, 0
    # r_t, c_t = 999, 999
    # S = ["." * W for _ in range(H)]

    graph = [[0 for _ in range(W)] for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if(S[h][w] == "."):
                for d in range(4):
                    hhh = h + OFFSET[d][0]
                    www = w + OFFSET[d][1]
                    if(0 <= hhh < H and 0 <= www < W and S[hhh][www] == "."):
                        graph[h][w] |= 1 << d

    mins = [[None for _ in range(W)] for _ in range(H)]
    mins[r_s][c_s] = 0
    search = [[r_s, c_s, 15]]
    while(True):
        search_tmp = []
        appends = []
        for h, w, d in search:
            for d2 in range(4):
                if(((graph[h][w] >> d2) & 1) == 1):
                    hhh = h + OFFSET[d2][0]
                    www = w + OFFSET[d2][1]
                    if(mins[hhh][www] is None):
                        search_tmp.append([hhh, www, 1 << d2])
                        appends.append([hhh, www, mins[h][w] + (0 if ((d >> d2) & 1) == 1 else 1)])
                        # mins[hhh][www] = [hhh, www, mins[h][w] + (0 if ((d >> d2) & 1) == 1 else 1)]
                    else:
                        mins[hhh][www] = min([mins[hhh][www], mins[h][w] + (0 if ((d >> d2) & 1) == 1 else 1)])
        for hhh, www, v in appends:
            mins[hhh][www] = v
        search = search_tmp
        if(len(search) == 0):
            break

    print(mins[r_t][c_t])


if(__name__ == "__main__"):
    main()
