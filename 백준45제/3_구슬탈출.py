import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def move(ri, rj, bi, bj, d):
    global hi, hj
    nri, nrj, nbi, nbj = ri, rj, bi, bj

    for i in range(1, 11):
        tri, trj = ri + dir[d][0] * i, rj + dir[d][1] * i
        if 0 <= tri < N and 0 <= trj < M:  # 배열 범위 체크 추가
            if arr[tri][trj] != '#':
                nri, nrj = tri, trj
                if arr[nri][nrj] == 'O':
                    break
            else:
                break

    for i in range(1, 11):
        tbi, tbj = bi + dir[d][0] * i, bj + dir[d][1] * i
        if 0 <= tbi < N and 0 <= tbj < M:  # 배열 범위 체크 추가
            if arr[tbi][tbj] != '#':
                nbi, nbj = tbi, tbj
                if arr[nbi][nbj] == 'O':
                    break
            else:
                break

    if (nri, nrj) == (hi, hj):  # 빨간 공이 구멍에 들어갔을 때
        return nri, nrj, nbi, nbj

    if (nri, nrj) == (nbi, nbj):  # 빨간 공과 파란 공이 같은 위치일 때
        if abs(nri - ri) + abs(nrj - rj) > abs(nbi - bi) + abs(nbj - bj):
            nri, nrj = nri - dir[d][0], nrj - dir[d][1]
        else:
            nbi, nbj = nbi - dir[d][0], nbj - dir[d][1]

    return nri, nrj, nbi, nbj

def bfs(ri, rj, bi, bj):
    global ans
    q = deque()
    q.append((ri, rj, bi, bj))
    v = dict()
    v[(ri, rj, bi, bj)] = 0

    while q:  # ✅ 수정: 큐가 비어있지 않을 때만 실행
        cri, crj, cbi, cbj = q.popleft()

        if (cbi, cbj) == (hi, hj):  # 파란 공이 구멍에 빠지면 무효
            continue
        elif (cri, crj) == (hi, hj):  # 빨간 공이 구멍에 들어가면 성공
            ans = v[(cri, crj, cbi, cbj)]
            return  # ✅ 수정: break 대신 return 사용

        if v[(cri, crj, cbi, cbj)] > 10:  # 10번 초과하면 실패
            ans = -1
            return

        for d in range(4):
            nri, nrj, nbi, nbj = move(cri, crj, cbi, cbj, d)
            if (nri, nrj, nbi, nbj) not in v:
                v[(nri, nrj, nbi, nbj)] = v[(cri, crj, cbi, cbj)] + 1
                q.append((nri, nrj, nbi, nbj))

    ans = -1  # ✅ 큐를 다 돌았는데 성공 못 하면 -1 반환

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = float('inf')

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            ri, rj = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            bi, bj = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'O':
            hi, hj = i, j

bfs(ri, rj, bi, bj)
print(ans)
