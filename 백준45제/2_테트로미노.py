import sys
sys.stdin = open('input.txt', 'r')

def in_range(ni, nj):
    return 0<=ni<N and 0<=nj<M

def dfs(n, lst, sm):
    global ans

    if sm+(3-n)*mx<ans:
        return
    if n==3:
        ans = max(ans, sm)
        return

    for i, j in lst:
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = i+di, j+dj
            if in_range(ni, nj) and not v[ni][nj]:
                v[ni][nj] = 1
                dfs(n+1, lst+[(ni, nj)], sm+arr[ni][nj])
                v[ni][nj] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = float('-inf')
mx = max(map(max, arr))
v = [[0]*(M+1) for _ in range(N)]

for i in range(N):
    for j in range(M):
        v[i][j] = 1
        dfs(0, [(i, j)], arr[i][j])
        v[i][j] = 0
print(ans)