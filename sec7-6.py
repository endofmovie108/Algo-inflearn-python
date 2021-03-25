# 문자열 관련 built-in: ord, chr 함수

import sys
sys.stdin = open('input.txt', 'rt')

in_str = input()
N = len(in_str)
A_ord = ord('A')-1
cnt = 0

def DFS(idx_start, full_str):
    global in_str, cnt
    if N==1 and in_str == '0':
        return
    if idx_start >= N:
        cnt += 1
        print(full_str)
        return
    # one character
    DFS(idx_start + 1, full_str + chr(int(in_str[idx_start:idx_start+1]) + A_ord))
    # two character
    if idx_start < N-1 and int(in_str[idx_start:idx_start+2]) <= 26:
        DFS(idx_start + 2, full_str + chr(int(in_str[idx_start:idx_start+2]) + A_ord))

DFS(0, "")
print(cnt)