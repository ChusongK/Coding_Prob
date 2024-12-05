# import sys
# sys.stdin = open('input.txt', 'r')
from collections import deque

M, N, H = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
v = [[[0]*M for _ in range(N)] for _ in range(H)]

q = deque()

def bfs():
    global arr

    while q:
        ck, cj, ci= q.popleft()
        for dk, dj, di in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
            nk, nj, ni = ck + dk, cj + dj, ci + di
            if 0<=nk<H and 0<=nj<N and 0<=ni<M and arr[nk][nj][ni]==0 and not v[nk][nj][ni]:
                v[nk][nj][ni] = 1
                arr[nk][nj][ni] = arr[ck][cj][ci] + 1
                q.append((nk, nj, ni))

for k in range(H):
    for j in range(N):
        for i in range(M):
            if arr[k][j][i]==1: # 익은게 있으면,
                q.append((k, j, i)) # q에 추가
                v[k][j][i] = 1  # 방문 표시
bfs()

for k in range(H):
    for j in range(N):
        for i in range(M):
            if arr[k][j][i]==0: # 안익은게 있으면,
                print(-1)
                exit(0)
ans = 0
for k in arr:
    for j in k:
        ans = max(ans, max(j))
print(ans-1)