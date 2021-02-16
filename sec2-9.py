import sys
#sys.stdin=open('input.txt', 'rt')
N=int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
res = [0]*N

for idx, dice in enumerate(dices):
    pal = [0] * 7
    max_pal = 0
    max_d = 0
    local_max_d = 0
    for d in dice:
        pal[d] += 1
        if d > local_max_d: local_max_d=d
        if pal[d] > max_pal:
            max_pal = pal[d]
            max_d = d

    if max_pal == 3:
        res[idx] = 10000+max_d*1000
    elif max_pal == 2:
        res[idx] = 1000+max_d*100
    else:
        res[idx] = local_max_d*100

print(max(res))