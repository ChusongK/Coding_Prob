import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if arr[i][j]=='R':
            ri, rj = i, j
        elif arr[i][j]=='B':
            bi, bj = i, j

def bfs(ri, rj, bi, bj):
    q = deque()
    q.append((ri, rj, bi, bj))
    v= set()
    v.add((ri, rj, bi, bj))
    cnt = 0

    while q:
        for _ in range(len(q)):
            ri, rj, bi, bj = q.popleft()
            if cnt>10:
                print(-1)
                return
            if arr[ri][rj]=='O':
                print(cnt)
                return
            for i in range(4):
                nri, nrj = ri, rj
                while True:
                    nri += dx[i]
                    nrj += dy[i]
                    if arr[nri][nrj]=='#':
                        nri -= dx[i]
                        nrj -= dy[i]
                        break
                    elif arr[nri][nrj]=='O':
                        break
                nbi, nbj = bi, bj
                while True:
                    nbi += dx[i]
                    nbj += dy[i]
                    if arr[nbi][nbj]=='#':
                        nbi -= dx[i]
                        nbj -= dy[i]
                        break
                    elif arr[nbi][nbj]=='O':
                        break
                if arr[nbi][nbj]=='O':
                    continue
                if (nri, nrj) == (nbi, nbj):
                    if abs(nri-ri)+abs(nrj-rj)>abs(nbi-bi)+abs(nbj-bj):
                        nri -= dx[i]
                        nrj -= dy[i]
                    else:
                        nbi -= dx[i]
                        nbj -= dy[i]
                if (nri, nrj, nbi, nbj) not in v:
                    q.append((nri, nrj, nbi, nbj))
                    v.add((nri, nrj, nbi, nbj))
        cnt += 1
    print(-1)
bfs(ri, rj, bi, bj)