import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
v = [[0]*N for _ in range(N)]
cnt = 0
ans = []

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_range(x, y):
    return 0<=x<N and 0<=y<N

def bfs(i, j):
    q = deque()
    q.append((i, j))
    v[i][j] = 1
    home_cnt = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in direction:
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and arr[ni][nj]==1 and v[ni][nj]==0:
                q.append((ni, nj))
                v[ni][nj] = 1
                home_cnt += 1
    ans.append(home_cnt)

for i in range(N):
    for j in range(N):
        if arr[i][j]==1 and v[i][j]==0:
            bfs(i, j)
            cnt += 1

print(cnt)
ans.sort()
for i in ans:
    print(i)
