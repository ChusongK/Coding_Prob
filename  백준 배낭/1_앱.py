import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
min_cost = sys.maxsize
DP = [[0]*(sum(cost)+1) for _ in range(N+1)]

for i in range(1, N+1):
    m, c = memory[i-1], cost[i-1]
    for j in range(sum(cost)+1):
        if j>=c:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-c]+m)
        else:
            DP[i][j] = DP[i-1][j]
        if DP[i][j]>=M:
            min_cost = min(min_cost, j)

print(min_cost)