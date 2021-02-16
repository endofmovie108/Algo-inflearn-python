import sys
#sys.stdin=open('input.txt', 'rt')
N, K = map(int, input().split())

k=0
for i in range(N):

    if N%(i+1)==0:
        k+=1
        if k==K:
            print(i+1)
            break
else:
    print(-1)