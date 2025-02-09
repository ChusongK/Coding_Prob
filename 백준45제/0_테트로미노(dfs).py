import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, sm, tlst):
    global ans
    # 가지치기: 남은 값이 모두 mx여도 ans 갱신 못하는 경우
    if sm+(4-n)*mx <= ans:
        return

    if n==4:
        ans = max(ans, sm)
        return

    for ci, cj in tlst: # 도형의 모든위치에서 네방향
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            # 범위내 미방문이면 다음단계로
            if 0<=ni<N and 0<=nj<M and not v[ni][nj]:
                v[ni][nj] = 1
                dfs(n+1, sm+arr[ni][nj], tlst+[(ni,nj)])
                v[ni][nj] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]
ans = 0
mx = max(map(max, arr))

for i in range(N):
    for j in range(M):  # 가능한 모든 위치에서 dfs 탐색
        v[i][j] = 1
        dfs(1, arr[i][j], [(i,j)])
print(ans)
