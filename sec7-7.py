import sys
from collections import deque
sys.stdin=open('input.txt', 'rt')

S, E = list(input().split())
E = int(E)
S = [int(S)]
S = deque(S)
C = [0]
C = deque(C)
steps = [-1, 1, 5]
cnt = 0

# 중복 제거 필요, 초기 현수의 위치 저장
chk = [0]*10000
chk[S[0]-1] = 1
while S:
    curr = S.popleft()
    curr_c = C.popleft()
    if curr == E:
        print(curr_c)
        break
    else:
        for s in steps:
            curr_t = curr + s
            if (curr_t >= 1 and curr_t <= 10000) and chk[curr_t-1] != 1:
                chk[curr_t - 1] = 1
                S.append(curr_t)
                C.append(curr_c + 1)
            else:
                continue
