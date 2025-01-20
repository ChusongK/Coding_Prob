import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input())))

ans = []
v = [[0]*N for _ in range(N)]

def in_range(x, y):
    return 0<=x<N and 0<=y<N

def bfs(i, j):
    v[i][j] = 1
    q = deque()
    q.append((i, j))
    cnt = 0

    while q:
        ci, cj = q.popleft()
        cnt += 1
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and not v[ni][nj] and arr[ni][nj]==1:
                q.append((ni, nj))
                v[ni][nj] = 1
    ans.append(cnt)

for i in range(N):
    for j in range(N):
        if arr[i][j]==1 and not v[i][j]:    # 미방문 집 발견시,
            bfs(i, j)

print(len(ans))
ans.sort()
for i in ans:
    print(i)
