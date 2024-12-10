import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]

v = [[0]*M for _ in range(N)]
n = N - 1
m = M - 1


def bfs():
    q = []
    q.append((0,0))
    v[0][0] = 1

    while q:
        ci, cj = q.pop(0)
        if (ci, cj)==(n, m):
            print(v[ci][cj])
        for di, dj in ((-1, 0),(1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]==1:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))
bfs()