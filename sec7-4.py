import sys
#sys.stdin=open('input.txt', 'rt')
T = int(input())
k = int(input())
coins = [list(map(int, input().split())) for _ in range(k)]

def DFS(l, sum):
    global cnt
    if sum > T:
        return
    if l>=k:
        if sum == T:
            cnt += 1
        return
    else:
        for i in range(coins[l][1]+1):
            DFS(l+1, sum+coins[l][0]*i)

cnt = 0
DFS(0, 0)
print(cnt)