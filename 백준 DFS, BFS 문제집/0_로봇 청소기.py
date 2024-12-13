import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
ri, rj, d = map(int, input().split())
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
arr = [list(map(int, input().split())) for _ in range(N)]

# 청소 했는지 표시 배열
v = [[0]*M for _ in range(N)]
cnt = 0

def op():
    global ri, rj, d

    is_none = True
    for i, j in direction:
        ni, nj = ri + i, rj + j
        # 주변 4칸 중 청소 안한 빈칸이 있는 경우,
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0 and v[ni][nj]==0:
            is_none = False
    if is_none:
        temp_d = (d + 2) % 4
        ni, nj = ri + direction[temp_d][0], rj + direction[temp_d][1]
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
            ri, rj = ni, nj
            return
        else:
            print(cnt)
            exit(0)
    else:
        d = (d - 1) % 4
        ni, nj = ri + direction[d][0], rj + direction[d][1]
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0 and v[ni][nj]==0:
            ri, rj = ni, nj
        return

while True:
    if v[ri][rj]==0:    # 현재 칸 청소 안 했다면,
        v[ri][rj] = 1   # 현재 칸 청소
        cnt += 1

    op()


