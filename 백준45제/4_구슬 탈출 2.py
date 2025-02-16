import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def move(d, ri, rj, bi, bj):
    nri, nrj = ri, rj
    nbi, nbj = bi, bj

    while True:
        nri, nrj = nri+di[d], nrj+dj[d]
        if arr[nri][nrj]=='#':
            nri, nrj = nri-di[d], nrj-dj[d]
            break
        elif arr[nri][nrj]=='O':
            break

    while True:
        nbi, nbj = nbi+di[d], nbj+dj[d]
        if arr[nbi][nbj]=='#':
            nbi, nbj = nbi-di[d], nbj-dj[d]
            break
        elif arr[nbi][nbj]=='O':
            break

    if arr[nri][nrj]=='O' and arr[nbi][nbj]=='O':
        return nri, nrj, nbi, nbj

    if (nri, nrj)==(nbi, nbj):
        if abs(nri-ri)+abs(nrj-rj)>abs(nbi-bi)+abs(nbj-bj):
            nri, nrj = nri-di[d], nrj-dj[d]
        else:
            nbi, nbj = nbi-di[d], nbj-dj[d]
    return nri, nrj, nbi, nbj

def bfs(ri, rj, bi, bj):
    global ans

    q = deque()
    q.append((ri, rj, bi, bj))
    v = set()
    v.add((ri, rj, bi, bj))
    cnt = 0

    while q:
        if cnt>10:
            return
        for _ in range(len(q)):
            cri, crj, cbi, cbj = q.popleft()
            if arr[cbi][cbj]=='O':
                continue
            if arr[cri][crj]=='O':
                ans = cnt
                return

            for d in range(4):
                nri, nrj, nbi, nbj = move(d, cri, crj, cbi, cbj)
                if (nri, nrj, nbi, nbj) not in v:
                    q.append((nri, nrj, nbi, nbj))
                    v.add((nri, nrj, nbi, nbj))
        cnt += 1

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]=='R':
            ri, rj = i, j
            arr[i][j] = '.'
        elif arr[i][j]=='B':
            bi, bj = i, j
            arr[i][j] = '.'
ans = -1
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
bfs(ri, rj, bi, bj)
print(ans)