import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    DP = [0]*(M+1)
    DP[0] = 1

    for coin in coins:
        for j in range(coin, M+1):
            DP[j] += DP[j-coin]
    print(DP[M])