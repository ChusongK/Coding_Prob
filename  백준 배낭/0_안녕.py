import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))
DP = [[0]*100 for _ in range(N+1)]

for i in range(1, N+1):
    current_L, current_J = L[i-1], J[i-1]
    for j in range(100):
        if j<current_L:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-current_L]+current_J)

print(DP[N][99])
