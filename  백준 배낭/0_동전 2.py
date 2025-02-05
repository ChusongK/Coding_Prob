import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
coins = list(int(input()) for _ in range(N))

INF = sys.maxsize  # 충분히 큰 값 설정

# DP[i] = i원을 만들기 위한 최소 동전 개수
DP = [INF] * (K + 1)
DP[0] = 0  # 0원을 만드는 동전 개수는 0개

for coin in coins:
    for i in range(coin, K + 1):
        DP[i] = min(DP[i], DP[i - coin] + 1)  # 현재 값과 (i-coin 만들기 + 1개 추가) 비교
    print(DP)
# K원을 만들 수 없는 경우 -1 출력
print(DP[K] if DP[K] != INF else -1)


