import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for i in range(N)] for j in range(H)]
direction = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
q = deque()

def in_range(z, y, x):
    return 0<=z<H and 0<=y<N and 0<=x<M

def bfs():
    while q:
        ck, cj, ci = q.popleft()
        for dk, dj, di in direction:
            nk, nj, ni = ck+dk, cj+dj, ci+di
            if in_range(nk, nj, ni) and arr[nk][nj][ni]==0:
                q.append((nk, nj, ni))
                arr[nk][nj][ni] = arr[ck][cj][ci] + 1

for k in range(H):
    for j in range(N):
        for i in range(M):
            if arr[k][j][i]==1:
                q.append((k, j, i))

bfs()

for k in range(H):
    for j in range(N):
        for i in range(M):
            if arr[k][j][i]==0:
                print(-1)
                exit(0)
mx = 0
for i in arr:
    for j in i:
      mx = max(mx, max(j))

print(mx-1)