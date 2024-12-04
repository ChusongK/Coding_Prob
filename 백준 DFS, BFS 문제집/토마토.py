# https://velog.io/@falling_star3/%EB%B0%B1%EC%A4%80Python-7569%EB%B2%88-%ED%86%A0%EB%A7%88%ED%86%A0

import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')

M, N, H = map(int, input().split())


# 모두 익어 있다면 0 출력
# 모두 익지는 못하면 -1 출력
# 모두 익을 때까지 최소 며칠이 걸리는지?

# BFS구현
# 3차원 배열을 생성해주고, 6방향(앞,뒤,상,하,좌,우)을 설정해준다.
# 1을 값으로 가지고 있는 배열의 위치를 큐에 담아준다.
# BFS로 6방향을 확인하며 익지않은 토마토(0)가 있을시 +1씩 해준다.
# 가장 큰 값-1 출력한다. (1부터 +1을 해가므로 day는 -1을 해주어야 한다.)
# 모든 토마토가 1일 경우 0을 출력한다.
# 익지않은 토마토(0)가 있을 시 -1을 출력한다.

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
v = [[[0] * M for _ in range(N)] for _ in range(H)]

q = deque()
ans = 0

def bfs():
    while q:
        k, j, i = q.popleft()
        for rk, rj, ri in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
            ni, nj, nk = i + ri, j + rj, k + rk
            # 주변에 미방문, 안익었으면,
            if 0<=ni<M and 0<=nj<N and 0<=nk<H and arr[nk][nj][ni]==0 and not v[nk][nj][ni]:
                q.append((nk, nj, ni))
                arr[nk][nj][ni] = arr[k][j][i] + 1
                v[nk][nj][ni] = 1

# 모두 1이 아닐 경우
for k in range(H):
    for j in range(N):
        for i in range(M):
            if arr[k][j][i]==1 and v[k][j][i]==0:   # 미방문, 익었으면,
                q.append((k, j, i)) # q에 추가
                v[k][j][i]= 1
bfs()

# 토마토 확인
for k in arr:
    for j in k:
        for i in j:
            if i==0:
                print(-1)
                exit(0)
        ans = max(ans, max(j))

print(ans-1)
