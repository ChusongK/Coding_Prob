# https://my-coding-notes.tistory.com/157
# https://supersfel.tistory.com/223
import sys
sys.stdin = open('input.txt', 'r')

n = int(input())    # 30이하, 추의 개수
weights = list(map(int, input().split()))   # 무게 순 추 무게들
max_weight = sum(weights)

m = int(input())   # 확인하고픈 구슬 개수
marbles = list(map(int, input().split()))   # 무게 순 구슬들

dp = [[0] * (max_weight + 1) for _ in range(n + 1)] # dp[i][j] : i개, 무게j
res = ''

def sol(cnt=0, cost=0):
    if dp[cnt][cost] == 1:return
    dp[cnt][cost] = 1
    if cnt == n:return

    sol(cnt+1, cost + weights[cnt])
    sol(cnt+1, cost)
    sol(cnt+1, abs(cost - weights[cnt]))
sol()

for marble in marbles:
    if marble > max_weight:res+='N '
    elif dp[n][marble]:res+='Y '
    else:res+='N '
print(res)
