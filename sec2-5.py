import sys
sys.stdin=open('input.txt', 'rt')
N, M=map(int, input().split())
cnts = [0]*(N+M+1)
for i in range(1, N+1):
    for j in range(1, M+1):
        cnts[i+j] += 1
#cnts.sort(reverse=True)
max_cnt = max(cnts)
for i in range(2, N+M+1):
    if max_cnt == cnts[i]:
        print(i, end=' ')