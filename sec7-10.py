import sys

sys.stdin = open('input.txt', 'rt')
N = 7
maps = [list(map(int, input().split())) for _ in range(N)]
chks = [[0]*N for _ in range(N)]

r_dirs = [-1, 0, 1, 0]
c_dirs = [0, 1, 0, -1]
chks[0][0] = 1
cnt = 0
def DFS(rr, cc, ll):
    global cnt

    if rr == N-1 and cc == N-1:
        cnt+=1
        return

    for i in range(4):
        r, c, l = rr + r_dirs[i], cc + c_dirs[i], ll + 1
        if ((r >= 0 and r <= N-1) and (c >= 0 and c <= N-1)) and chks[r][c] == 0 and maps[r][c] == 0:

            chks[r][c] = 1
            DFS(r, c, l)
            chks[r][c] = 0 # 방문 후 체크해제 필!
DFS(0, 0, 0)
print(cnt)