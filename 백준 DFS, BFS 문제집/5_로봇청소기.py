import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
R, C, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
cnt = 0

while True:
    if arr[R][C]==0:
        arr[R][C] = -1
        cnt += 1

    for _ in range(4):
        D = (D-1)%4
        nr, nc = R+di[D], C+dj[D]
        if arr[nr][nc]==0:
            R, C = nr, nc
            break
    else:
        tr, tc = R+di[(D+2)%4], C+dj[(D+2)%4]
        if arr[tr][tc]!=1:
            R, C = tr, tc
        else:
            break
print(cnt)