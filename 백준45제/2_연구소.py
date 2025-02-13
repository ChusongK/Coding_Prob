import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def in_range(ni, nj):
    return 0<=ni<N and 0<=nj<M

def bfs(lst):
    global mx
    for i, j in lst:
        arr[i][j] = 1

    cnt = CNT-3
    q = deque()
    v = [[0]*M for _ in range(N)]
    for i, j in virus:
        q.append((i, j))
        v[i][j] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if in_range(ni, nj) and not v[ni][nj] and arr[ni][nj]==0:
                q.append((ni, nj))
                v[ni][nj] = 1
                cnt -= 1
    mx = max(mx, cnt)
    for i, j in lst:
        arr[i][j] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = [(i, j) for i in range(N) for j in range(M) if arr[i][j]==2]
empty = [(i, j) for i in range(N) for j in range(M) if arr[i][j]==0]
mx = 0
CNT = len(empty)

for i in range(CNT-2):
    for j in range(i+1, CNT-1):
        for k in range(j+1, CNT):
            bfs([empty[i], empty[j], empty[k]])
print(mx)