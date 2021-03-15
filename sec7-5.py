import sys
#sys.stdin=open('input.txt', 'rt')
N = int(input())
coins = [int(input()) for _ in range(N)]
#print(coins)

def DFS(l, A, B, C):
    global min_val
    if l>=N:
        tmp = abs(max(A, B, C) - min(A, B, C))
        if (A != B) and (A != C) and (B != C) and tmp < min_val:
            min_val = tmp
        return
    DFS(l + 1, A + coins[l], B, C)
    DFS(l + 1, A, B + coins[l], C)
    DFS(l + 1, A, B, C + coins[l])

min_val = 1e+10
DFS(0, 0, 0, 0)
print(min_val)