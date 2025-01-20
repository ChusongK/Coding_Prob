# 높이는 1이상 100 이하의 정수라고 했으니,
# 1의 높이를 가진 타일이 있을 경우,
# 높이가 0이하인 지점을 모두 잠기게 만드는 비가 내리는 조건이
# loop에 있어야 아무 지역도 물에 잠기지 않는다는 조건을 충족 할 수 있음.

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
mx = 1
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = []

for i in arr:
    mx = max(mx, max(i))

def in_range(x, y):
    return 0<=x<N and 0<=y<N

def bfs(i, j, k):
    v[j][k] = 1
    q = deque()
    q.append((j, k))

    while q:
        ci, cj = q.popleft()
        for di, dj in directions:
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and not v[ni][nj] and arr[ni][nj]>i:
                q.append((ni, nj))
                v[ni][nj] = 1

for i in range(mx+1):
    cnt = 0
    v = [[0]*N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            if arr[j][k]>i and not v[j][k]:    # 미방문, 안잠겼으면,
                bfs(i, j, k)
                cnt += 1
    ans.append(cnt)

print(max(ans))