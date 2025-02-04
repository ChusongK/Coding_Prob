# https://hongcoding.tistory.com/50
import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
DP = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    w, v = items[i-1]
    for j in range(1, K+1):
        if j<w:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(DP[i-1][j], v+DP[i-1][j-w])
print(DP[N][K])