import sys
sys.stdin = open('input.txt', 'r')

def in_range(ni, nj):
    return 0<=ni<R and 0<=nj<C

R, C, M = map(int, input().split())
arr = [[0]*C for _ in range(R)]
dir = {1:2,2:1,3:4,4:3}
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, 1, -1]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    arr[r-1][c-1] = (s, d, z)

ans = 0
for j in range(C):
    # 낚시
    for i in range(R):
        if arr[i][j]:   # 열에 상어 발견시,
            ans += arr[i][j][2] # 먹고,
            arr[i][j] = 0   # out.
            break       # 한번 먹으면 이동.
    # 상어 이동
    narr = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j]:   # 상어발견시 이동.
                s, d, z = arr[i][j]
                ni, nj = i, j
                for _ in range(s):  # 속도 만큼 이동.
                    ni, nj = ni+di[d], nj+dj[d]
                    if not in_range(ni, nj):    # 범위 밖이면,
                        d = dir[d]  # 방향 반대로
                        ni, nj = ni+di[d]*2, nj+dj[d]*2 # 두칸 가서 복원
                # narr에 반영
                if narr[ni][nj]==0: # 비었으면,
                    narr[ni][nj] = (s, d, z)    # 이동
                else: # 상어 존재시,
                    if narr[ni][nj][2]<z:   # 이동해 온게 더 크다면,
                        narr[ni][nj] = (s, d, z)  # 이동
    arr = narr  # 이동 반영
print(ans)