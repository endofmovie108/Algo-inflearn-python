import sys
from collections import deque

sys.stdin = open('input.txt', 'rt')

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
chks = [[0]*N for _ in range(N)]
total_sum = 0
r_dirs = [-1, 0, 1, 0]
c_dirs = [0, 1, 0, -1]

apples = deque()
apples.append([maps[N//2][N//2], N//2, N//2, 1]) # apple, row, col, level
chks[N//2][N//2] = 1
total_sum += maps[N//2][N//2]

while apples:
    apple, rr, cc, lv = apples.popleft()
    if lv <= N//2:
        for i in range(4):
            r = rr + r_dirs[i]
            c = cc + c_dirs[i]
            if chks[r][c] == 0:
                total_sum += maps[r][c]
                chks[r][c] = 1
                apples.append([maps[r][c], r, c, lv+1])

print(total_sum)


