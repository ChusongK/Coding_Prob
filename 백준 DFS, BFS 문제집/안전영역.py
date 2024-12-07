import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0

mx = 0
for i in arr:
    mx = max(max(i), mx)

def bfs(i, j):
    global v

    q = deque()
    q.append((i, j))
    v[i][j] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]>t:
                q.append((ni, nj))
                v[ni][nj] = 1

# 장마 루프 시작
for t in range(0, mx+1):
    # 매 루프마다 당연히 방문배열을 최신화해줘야함.
    v = [[0] * N for _ in range(N)]
    cnt = 0
    # 배열 순회 하면서 bfs (미방문, 안 잠겼다면,)
    for i in range(N):
        for j in range(N):
            if v[i][j]==0 and arr[i][j]>t:
                bfs(i, j)
                cnt += 1
    ans = max(ans, cnt)

print(ans)