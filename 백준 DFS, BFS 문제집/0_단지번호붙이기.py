import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
ans = []

def bfs(i, j):
    global arr, ans
    q = [(i, j)]
    cnt = 1
    arr[i][j] = 0  # 집 방문 후 초기화 (방문 표시)

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            # 범위내, 미방문이자 갈 수 있다면,
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1:
                q.append((ni, nj))
                arr[ni][nj] = 0 # 집 방문 후 초기화 (방문 표시)
                cnt += 1

    ans.append(cnt)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            bfs(i, j)

print(len(ans))
ans.sort()
for i in ans:
    print(i)

# for i in arr:
#     print(i)