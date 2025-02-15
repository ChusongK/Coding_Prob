import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j]=='R':
            ri, rj = i, j
            arr[i][j] = '.'
        elif arr[i][j]=='B':
            bi, bj = i, j
            arr[i][j] = '.'
        elif arr[i][j]=='O':
            hi, hj = i, j

print(hi, hj)