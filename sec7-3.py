# 7-3

import sys
from collections import deque
sys.stdin=open('input.txt', 'rt')
N=int(input())
choo=list(map(int, input().split()))

choo_l = []
choo_r = []

def DFS_choo(l):
    if l>=N:
        choo_res.append(abs(sum(choo_l)-sum(choo_r)))
        return
    # 왼쪽과 오른쪽 두 팔 모두에 올리지 않는 경우
    DFS_choo(l+1)

    # 왼쪽 팔에 올리는 경우
    choo_l.append(choo[l])
    DFS_choo(l+1)
    choo_l.pop()

    # 오른쪽 팔에 올리는 경우
    choo_r.append(choo[l])
    DFS_choo(l+1)
    choo_r.pop()

choo_res = []
DFS_choo(0)
choo_res = set(choo_res)
print(sum(choo) - (len(choo_res)-1))