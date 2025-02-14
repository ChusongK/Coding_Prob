import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0

while True:
    if arr[r][c] == 0:
        cnt += 1
        arr[r][c] = -1

    is_exist = False

    for _ in range(4):
        d = (d - 1) % 4
        ni, nj = r + dir[d][0], c + dir[d][1]
        if arr[ni][nj] == 0:
            is_exist = True
            r, c = r + dir[d][0], c + dir[d][1]
            break

    if not is_exist:
        ni, nj = r + dir[(d + 2) % 4][0], c + dir[(d + 2) % 4][1]
        if arr[ni][nj] <= 0:
            r, c = ni, nj
        elif arr[ni][nj] == 1:
            print(cnt)
            exit(0)
