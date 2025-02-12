import sys
sys.stdin = open('input.txt', 'r')

def in_range(nx,ny):
    return 0<=nx<N and 0<=ny<M

def dfs(n, lst, sm):
    global ans
    # 가지치기: 남은 값이 모두 mx여도 ans 갱신 못하는 경우
    if sm+(4-n)*mx <= ans:
        return

    if n==4:
        ans = max(ans, sm)
        return

    for i, j in lst:
        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni, nj = i+di, j+dj
            if in_range(ni, nj) and not v[ni][nj]:
                v[ni][nj] = 1
                dfs(n+1, lst+[[ni, nj]], sm+arr[ni][nj])
                v[ni][nj] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
mx = max(map(max, arr))
v = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        v[i][j] = 1
        dfs(1, [[i, j]], arr[i][j])
print(ans)
