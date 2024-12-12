import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ice = set()

for i in range(N):
    for j in range(M):
        if arr[i][j]>0:
            ice.add((i, j))

print(sum(arr[i][j] for i, j in ice))