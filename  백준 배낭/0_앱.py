# https://wooono.tistory.com/603
import sys
sys.stdin = open('input.txt','r')

N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
res = sys.maxsize
DP = [[0]*(sum(cost)+1) for _ in range(len(cost)+1)]

for i in range(1, len(cost)+1):
    m, c = memory[i-1], cost[i-1]
    for j in range(sum(cost)+1):
        if j<c:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(DP[i-1][j], m+DP[i-1][j-c])
        if DP[i][j]>=M:
            res = min(res, j)
print(res)
