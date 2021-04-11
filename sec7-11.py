import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())

r_dirs = [-1, 0, 1, 0]
c_dirs = [0, 1, 0, -1]
maps = []
chks = [[0]*N for _ in range(N)]
max_val = -1
min_rr, min_cc = 0, 0
min_val = 1e+10
max_rr, max_cc = 0, 0
for rr in range(N):
    tmp = list(map(int, input().split()))
    maps.append(tmp)
    for cc in range(N):
        tmp_val = maps[rr][cc]
        if tmp_val > max_val:
            max_val = tmp_val
            max_rr, max_cc = rr, cc
        if tmp_val < min_val:
            min_val = tmp_val
            min_rr, min_cc = rr, cc

def DFS(rr, cc, ll):
    global cnt, max_rr, max_cc
    if rr == max_rr and cc == max_cc:
        cnt += 1
        return
    else:
        h_val = maps[rr][cc]
        for i in range(4):
            r, c, l, = rr + r_dirs[i], cc + c_dirs[i], ll + 1

            if r>=0 and r<=N-1 and c>=0 and c<=N-1 and chks[r][c] == 0 and maps[r][c] > h_val:
                chks[r][c] = 1
                DFS(r, c, l)
                chks[r][c] = 0

cnt = 0
chks[min_rr][min_cc] = 1
DFS(min_rr, min_cc, 0)
print(cnt)