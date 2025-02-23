import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def in_range(ni, nj):
    return 0<=ni<N and 0<=nj<N

def bfs(i, j):
    q = deque()
    v[i][j] = 1
    q.append((i, j))
    tlst = []
    tlst.append((i, j))
    total = A[i][j]

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if in_range(ni, nj) and not v[ni][nj] and \
                L<=abs(A[ci][cj] - A[ni][nj])<=R:
                q.append((ni, nj))
                tlst.append((ni, nj))
                total += A[ni][nj]
                v[ni][nj] = 1

    new_num = total//len(tlst)
    for ti, tj in tlst:
        A[ti][tj] = new_num

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

day = 0
while True:
    move_exist = False
    v = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if v[i][j]: continue
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni, nj = i+di, j+dj
                if in_range(ni,nj) and not v[ni][nj] and \
                    L<=abs(A[i][j]-A[ni][nj])<=R:
                    move_exist = True
                    bfs(i, j)
                    break
    if move_exist:
        day += 1
    else:
        break
print(day)