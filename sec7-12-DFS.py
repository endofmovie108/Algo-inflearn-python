import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())
maps = []

r_dirs = [-1, 0, 1, 0]
c_dirs = [0, 1, 0, -1]
for i in range(N):
    tmp = input()
    tmp_map = []
    M = len(tmp)
    for j in range(M):
        tmp_map.append(int(tmp[j]))
    maps.append(tmp_map)

def DFS(r, c):
    global aptnum
    for i in range(4):
        rr, cc = r + r_dirs[i], c + c_dirs[i]
        if rr>=0 and rr<=N-1 and cc>=0 and cc<=N-1 and maps[rr][cc]==1:
            maps[rr][cc] = 0
            aptnum += 1
            DFS(rr, cc)

danji = 0
aptnums = []
for r_idx in range(N):
    for c_idx in range(N):
        if maps[r_idx][c_idx] == 1:
            danji += 1
            aptnum = 0
            DFS(r_idx, c_idx)
            aptnums.append(aptnum)

print(danji)
aptnums.sort()
for aptnum in aptnums:
    print(aptnum)