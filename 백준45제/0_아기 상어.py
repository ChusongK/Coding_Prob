import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(ti, tj):
    q = deque()
    si, sj = shk[0],shk[1]
    q.append((si,sj))
    v = [[0]*N for _ in range(N)]
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        if (ci, cj)==(ti, tj):
            return v[ci][cj]-1
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and not v[ni][nj] and arr[ni][nj]<=size:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
    return -1   # 작은 고기는 있는데 갈 수가 없어서 못먹는 경우 -1 반환

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
t = 0
size = 2
cnt = 0
fish = set()
for i in range(N):
    for j in range(N):
        if arr[i][j]==9:
            shk = (i, j)
            arr[i][j] = 0
        elif 1<=arr[i][j]<=6:
            fish.add((i, j))

while True:
    poss = []
    for i, j in fish:
        if arr[i][j]<size:
            poss.append((i, j))
    NUM = len(poss)

    if NUM==0:
        break
    else:
        mn = float('inf')
        for i, j in poss:
            res = bfs(i, j)
            if res==-1:
                continue
            if NUM==1:
                mn = res
                tg = (i, j)
                break
            if res<mn:
                mn = res
                tg = (i, j)
            elif res==mn:
                if (i<tg[0]) or (i==tg[0] and j<tg[1]):
                    tg = (i, j)
    if mn==float('inf'):    # 작은 고기는 있는데 갈 수가 없어서 못 먹는 다면,
        break

    a, b = tg[0], tg[1]
    shk = (a, b)
    cnt += 1
    if size==cnt:
        size += 1
        cnt = 0
    arr[a][b] = 0
    t += mn
    fish.remove((a, b))
print(t)