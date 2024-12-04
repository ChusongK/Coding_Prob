import sys
sys.stdin = open('input.txt', 'r')

M, N, H = map(int, input().split())


# 모두 익어 있다면 0 출력
# 모두 익지는 못하면 -1 출력
# 모두 익을 때까지 최소 며칠이 걸리는지?

# 배열 어떻게 저장?
# bfs 어떻게?
# 턴 시작마다 다 익었는지 체크?

arr = []
for _ in range(H):
    temp = []
    for _ in range(N):
       temp.append(list(map(int, input().split())))
    arr.append(temp)

# print(arr)

t = 0
not_done_cnt = 0

def find_n_change(k, j, i):
    global arr, v

    for rk, rj, ri in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
        ni, nj, nk = i + ri, j + rj, k + rk
        if 0<=ni<M and 0<=nj<N and 0<=nk<H and arr[nk][nj][ni]==0:
            arr[nk][nj][ni] = 1
            v[nk][nj][ni] = 1



while True:
    is_all_done = True

    temp = 0
    for k in range(H):
        for j in range(N):
            for i in range(M):
                if arr[k][j][i]==0: # 안익은게 있으면,
                    is_all_done = False # 다 안익었으면 플래그 변경
                    temp += 1   # 이번턴 안익은 개수 세기

    if is_all_done: # 다 익었으면,
        if t==0:    # 처음부터 다 익어 있었다면,
            print(0)    # 0 출력
        else:
            print(t)    # 걸린 턴수 출력
        break

    if t==0:    # 첫 턴이면,
        not_done_cnt = temp # 안익은 개수 업데이트
    else:       # 이후 턴이면,
        if not_done_cnt==temp:  # 안익은 개수가 전과 같다면,
            print(-1)   # -1 출력
            break
        else:   # 더 익은게 있다면,
            not_done_cnt = temp # 안익은 개수 업데이트

    v = [[[0] * M for _ in range(N)] for _ in range(H)]

    for k in range(H):
        for j in range(N):
            for i in range(M):
                if arr[k][j][i]==1 and not v[k][j][i]: # 미방문, 익은게 있으면,
                    v[k][j][i] = 1
                    find_n_change(k, j, i)  # 주변 탐색해서 변경

    t += 1

# print(v)