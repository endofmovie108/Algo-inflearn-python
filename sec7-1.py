import sys
#sys.stdin=open('input.txt', 'rt')
# 각 문제들은 풀거나, 안풀거나의 두 가지 상황이 가능하다.
# 부분집합 문제로 생각해도 된다.

N, M = map(int, input().split())
SNTs = [list(map(int, input().split())) for _ in range(N)]

def DFS(l, sum_s, sum_t):
    global max_score
    if sum_t > M:
        return
    if l == N:
        if sum_s > max_score:
            max_score = sum_s
        return
    else:
        # 해당 문제를 풀경우
        DFS(l+1, sum_s + SNTs[l][0], sum_t + SNTs[l][1])
        # 해당 문제를 풀지 않을경우
        DFS(l+1, sum_s, sum_t)

max_score = 0
DFS(0, 0, 0)
print(max_score)