# K번째 큰 수
# set의 활용(중복 제거)

import sys
#sys.stdin=open('input.txt', 'rt')
N, K = map(int, input().split())
cards = list(map(int, input().split()))
ss = set()
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            ss.add(cards[i] + cards[j] + cards[k])
ss = list(ss)
ss.sort(reverse=True)
print(ss[K-1])