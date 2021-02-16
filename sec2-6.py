import sys
sys.stdin=open('input.txt', 'rt')
N = int(input())
nums = map(int, input().split())
sums = [0]*N
max_sum = 0

for num_idx, num in enumerate(nums):
    num_str = '%d' % (num)

    for ns in num_str:
        sums[num_idx] += int(ns)

    if sums[num_idx] > max_sum:
        max_sum = sums[num_idx]
        max_num = num

print(max_num)