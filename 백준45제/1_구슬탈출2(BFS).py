# https://bgspro.tistory.com/70
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j]=='R':
            rx, ry = i, j
        elif arr[i][j]=='B':
            bx, by = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    v = []
    v.append((rx, ry, bx, by))
    cnt = 0

    while q:
        for _ in range(len(q)):
            crx, cry, cbx, cby = q.popleft()
            if cnt>10:  # 10번 이하로 움직여서 빨구슬 못 빼면,
                print(-1)
                return
            if arr[crx][cry]=='O':  # 빨구가 빠지면,
                print(cnt)
                return
            for i in range(4):  # 네방향 탐색
                nrx, nry = crx, cry # 빨구 좌표 초기화
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if arr[nrx][nry]=='#':  # 벽이면,
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    elif arr[nrx][nry]=='O': # 구멍이면,
                        break
                nbx, nby = cbx, cby
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if arr[nbx][nby]=='#':  # 벽이면,
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    elif arr[nbx][nby]=='O': # 구멍이면,
                        break
                if arr[nbx][nby]=='O':  # 파가 구멍이면,
                    continue    # 무시하고 다른 방향 탐색
                if (nrx, nry) == (nbx, nby):    # 두구슬이 겹치면,
                    if abs(nrx-crx)+abs(nry-cry)>abs(nbx-cbx)+abs(nby-cby):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in v:
                    q.append((nrx, nry, nbx, nby))
                    v.append((nrx, nry, nbx, nby))
        cnt += 1
    print(-1)
bfs(rx, ry, bx, by)
