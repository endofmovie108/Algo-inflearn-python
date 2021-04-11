import sys
from collections import deque
sys.stdin = open('input.txt', 'rt')

N = 7
r_dirs = [-1, 0, 1, 0]
c_dirs = [0, 1, 0, -1]

maps = [list(map(int, input().split())) for _ in range(N)]
chks = [[0]*N for _ in range(N)]
curr_loc = deque()
curr_loc.append([0, 0, 0]) # row, col, level

while curr_loc:
    rr, cc, ll = curr_loc.popleft()
    for i in range(4):
        r, c, l = rr + r_dirs[i], cc + c_dirs[i], ll+1
        if (r >= 0 and r <= N-1) and (c >= 0 and c <= N-1):
            if maps[r][c] == 0 and chks[r][c] == 0:

                if r == N-1 and c == N-1:
                    print(l)
                    sys.exit()

                chks[r][c] = 1
                curr_loc.append([r, c, l])
else:
    print(-1)
