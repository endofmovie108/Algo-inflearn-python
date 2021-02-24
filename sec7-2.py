# 미완성!

# 이 문제 또한
# 각각의 상담을 진행하거나, 진행하지 않거나의 두 가지 상황이 존재한다.
# 하지만, 각각의 상담들은 상담 기간이 존재하기 때문에
# 해당 상담 이후에 진행할 수 있는 상담의 후보는 상담진행 기간 이후의 상담들이 된다.

import sys
sys.stdin=open('input.txt', 'rt')
N = int(input())
tps = [list(map(int, input().split())) for _ in range(N)]

def DFS(st_t, sum_p):
    global N, max_money
    if st_t >= N+1:
        if sum_p > max_money:
            max_money = sum_p
        return
    # st_t 부터 탐색
    for t_idx in range(st_t, N):
        # 상담을 처리
        # 다음번의 st_t는 해당 상담을 처리하기 위해 필요한 기간을 더해줘야한다. (그리고, +1일)
        DFS(st_t + tps[t_idx][0]+1, sum_p + tps[t_idx][1])

        # 상담을 미처리
        # 이 다음번의 상담을 탐색하기 위해 st_t에 +1을 해줌.
        DFS(st_t + 1, sum_p)

max_money = 0
DFS(0, 0)
print(max_money)
