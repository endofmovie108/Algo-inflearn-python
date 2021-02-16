# 대표값
# 소숫점 첫재짜리 반올림 round()
import sys
sys.stdin=open('input.txt', 'rt')
N = map(int, input().split())
scores = list(map(int, input().split()))
score_avg = round(sum(scores)/len(scores), 0)

min_diff = 999999999999
max_score = 0

for idx, score in enumerate(scores):
    diff = abs(score - score_avg)
    if diff < min_diff:
        min_diff = diff
        min_idx = idx
        max_score = score
    elif diff == min_diff and score > max_score:
        min_idx = idx
        max_score = score

print('%d'%score_avg, min_idx+1)
