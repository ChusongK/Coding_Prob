import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
courses = [tuple(map(int, input().split())) for _ in range(K)]
DP = [[0]*(N+1) for _ in range(K+1)]
for i in range(1, K+1):
    importance, time = courses[i-1][0], courses[i-1][1]
    for j in range(1, N+1):
        if j>=time:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-time]+importance)
        else:
            DP[i][j] = DP[i-1][j]

print(DP[K][N])