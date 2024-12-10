import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
v = [[0]*M for _ in range(N)]

ei, ej = N-1, M-1
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_range(x, y):
    return 0<=x<N and 0<=y<M

def bfs():
    q = deque()
    q.append((0, 0))
    v[0][0] = 1

    while q:
        ci, cj = q.popleft()
        if (ci, cj)==(ei, ej):
            print(v[ci][cj])
            break
        for di, dj in direction:
            ni, nj = ci + di, cj + dj
            # 범위내, 갈 수 있고, 미방문이면,
            if in_range(ni, nj) and arr[ni][nj]==1 and v[ni][nj]==0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1

bfs()