import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input())))

def in_range(x, y):
    return 0<=x<N and 0<=y<M

def bfs():
    v = [[0]*M for _ in range(N)]
    v[0][0] = 1
    q = deque()
    q.append((0, 0))

    while q:
        ci, cj = q.popleft()
        if (ci, cj)==(N-1, M-1):
            print(v[ci][cj])
            exit(0)

        for ri, rj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + ri, cj + rj
            if in_range(ni, nj) and arr[ni][nj]==1 and not v[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1

bfs()