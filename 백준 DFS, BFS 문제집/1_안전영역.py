import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
mx = 1
for i in arr:
    mx = max(mx, max(i))

ans = 0

def in_range(x, y):
    return 0<=x<N and 0<=y<N

def bfs(i, j, v, h):
    q = deque()
    q.append((i, j))
    v[i][j] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in directions:
            ni, nj = ci+di, cj+dj
            if in_range(ni, nj) and v[ni][nj]==0 and arr[ni][nj]>h:
                q.append((ni, nj))
                v[ni][nj] = 1

def count_no(h):
    v = [[0] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j]>h and v[i][j]==0: # 안잠겼고, 미방문이면,
                bfs(i, j, v, h)
                cnt += 1

    return cnt

for h in range(mx+1):
    cnt_res = count_no(h)
    ans = max(ans, cnt_res)

print(ans)