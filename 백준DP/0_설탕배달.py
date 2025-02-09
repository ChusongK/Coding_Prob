# https://aia1235.tistory.com/88

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
INF = int(10e9)
## 이게 key 다
DP = [INF]*5001

DP[3] = DP[5] = 1

for i in range(6, N+1):
    # 3 또는 5kg 짜리 봉지 가져갈 수 있기 때문에 3kg 또는 5kg뺀 값 중 더 작은
    DP[i] = min(DP[i-3], DP[i-5]) + 1

if DP[N]<INF:
    print(DP[N])
else:
    print(-1)
print(DP[:20])