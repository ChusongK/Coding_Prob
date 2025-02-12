import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def in_range(ni, nj):
    return 0<=ni<N and 0<=nj<M

def bfs(lst):
    for i, j in lst:
        arr[i][j] = 1

    v_bfs = [[0] * M for _ in range(N)]
    q = deque()
    cnt = len(empty) - 3    # 남은 0의 개수(max값 찾을 변수)

    for i, j in virus:
        q.append((i, j))
        v_bfs[i][j] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if in_range(ni, nj) and not v_bfs[ni][nj] and arr[ni][nj]==0:
                q.append((ni, nj))
                v_bfs[ni][nj] = 1
                cnt -= 1

    for i, j in lst:
        arr[i][j] = 0

    return cnt

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
mx = 0
empty = [(i, j) for i in range(N) for j in range(M) if arr[i][j]==0]
virus = [(i, j) for i in range(N) for j in range(M) if arr[i][j]==2]
CNT = len(empty)
v = [0]*CNT

for i in range(CNT-2):
    for j in range(i+1, CNT-1):
        for k in range(j+1, CNT):
            mx = max(mx, bfs([empty[i], empty[j], empty[k]]))

print(mx)
