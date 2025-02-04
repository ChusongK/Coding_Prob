# https://didu-story.tistory.com/440
import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

DP = [0]*(K+1)
DP[0] = 1

for coin in coins:
    for i in range(coin, K+1):
            DP[i] += DP[i-coin]
print(DP[K])