"""
두 덩이 이상! 분리되는 최초의 시간(년)을 구하는건데
나는 2개 초과로 해서 틀림.
0으로 둘러싸여 있기 때문에 in_range(x,y)는 없어도 됨.
"""

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
t = 0

def count_0(i, j):
    cnt = 0
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = i + di, j + dj
        if arr[ni][nj]==0:  # 바다를 만나면,
            cnt += 1
    return cnt

def bfs(i, j):
    v[i][j] = 1
    q = deque()
    q.append((i, j))

    while q:
        ci, cj = q.popleft()
        for di, dj in directions:
            ni, nj = ci + di, cj + dj
            if arr[ni][nj]>0 and not v[ni][nj]: # 미방문, 빙하면,
                q.append((ni, nj))
                v[ni][nj] = 1

while True:
    t += 1
    narr = [x[:] for x in arr]
    for i in range(N):
        for j in range(M):
            if arr[i][j]!=0:    # 빙산을 만나면,
                narr[i][j] = max(0, narr[i][j] - count_0(i, j))
    arr = narr

    cnt_ice = 0
    v = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j]>0 and not v[i][j]:
                bfs(i, j)
                cnt_ice += 1
    if cnt_ice>=2:
        print(t)
        exit(0)
    elif cnt_ice==0:
        print(0)
        exit(0)