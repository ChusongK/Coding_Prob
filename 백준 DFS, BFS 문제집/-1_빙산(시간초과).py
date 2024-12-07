import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def search_n_subtract(i, j, arr, narr):
    cnt = 0
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = i + di, j + dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:  #바다 찾으면
            cnt += 1    # 바다 개수 카운트
    narr[i][j] = max(0, narr[i][j] - cnt)

    return narr

def bfs(i, j, arr, v):
    q = deque()
    q.append((i, j))
    v[i][j] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj]!=0 and v[ni][nj]==0:  # 빙산 찾고, 미방문이면!!!
                q.append((ni, nj))
                v[ni][nj] = 1
    return v

t = 0
while True:
    t += 1

    # 배열 복사
    narr = [x[:] for x in arr]
    cnt = 0
    # 배열 순회하면서 빙산 찾고, 찾으면 주변 0 개수 세서 narr에서 0 될때까지 빼기
    for i in range(1, N-1):
        for j in range(1, M-1):
            if arr[i][j]>0:  # 빙산 찾으면,
                narr = search_n_subtract(i, j, arr, narr)
                cnt += 1
    if cnt==0:
        print(0)
        break

    # 배열 갱신
    arr = [x[:] for x in narr]

    cnt2 = 0
    v = [[0]*M for _ in range(N)]
    # 분리되었는지 확인
    for i in range(1, N-1):
        for j in range(1, M-1):
            if arr[i][j]!=0 and v[i][j]==0:  # 빙산 찾고, !!!미방문이면!!!
                v = bfs(i, j, arr, v)
                cnt2 += 1 # 한덩이 추가

    if cnt2>=2:
        print(t)
        break

