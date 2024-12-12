import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ice = set()

for i in range(N):
    for j in range(M):
        if arr[i][j]>0:
            ice.add((i, j))

def in_range(x, y):
    return 0<=x<N and 0<=y<M

def find_ice_n_melt():
    # 주변 바다 찾아 빙산별 녹일 횟수 저장
    ice_to_melt = set()

    for i, j in ice:
        cnt = 0

        for di, dj in directions:
            ni, nj = i+di, j+dj
            if in_range(ni, nj) and arr[ni][nj]==0:  # 바다 있으면
                cnt += 1
        if cnt>0:
            ice_to_melt.add((i, j, cnt))

    # 녹이기
    for i, j, cnt in ice_to_melt:
        arr[i][j] = max(0, arr[i][j] - cnt)
        if arr[i][j]==0:
            ice.remove((i, j))

def bfs(i, j, v):
    q = deque()
    q.append((i, j))
    v.add((i, j))

    while q:
        ci, cj = q.popleft()
        for di, dj in directions:
            ni, nj = ci+di, cj+dj
            if in_range(ni, nj) and (ni, nj) not in v and (ni, nj) in ice:
                q.append((ni, nj))
                v.add((ni, nj))

def count_group():
    v = set()
    cnt = 0

    for i, j in ice:
        if (i, j) not in v:
            bfs(i, j, v)
            cnt += 1

    return cnt

t = 0
ans = 0

while True:
    t += 1
    # print(t, "년을 시작합니다.")
    find_ice_n_melt()

    if sum(arr[i][j] for i, j in ice)==0:
        print(0)
        break

    if count_group()>=2:
        print(t)
        break

# 빙산이 분리되는 최초의 시간(년)을 출력
# 만일 빙산이 다 녹을 때까지 분리되지 않으면 0을 출력