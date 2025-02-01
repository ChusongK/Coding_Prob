import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
lst = [tuple(map(int, input().split())) for _ in range(K)]

DP = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        DP[i][j] = DP[i][j-1] + DP[i-1][j] - DP[i-1][j-1] + arr[i-1][j-1]

for i, j, x, y in lst:
    ans = DP[x][y] - DP[x][j-1] - DP[i-1][y] + DP[i-1][j-1]
    print(ans)