import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
T = []
P = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
dp = [0]*(N+1)

for i in range(N-1, -1, -1):
    if i+T[i]>N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+T[i]]+P[i], dp[i+1])

print(dp[0])