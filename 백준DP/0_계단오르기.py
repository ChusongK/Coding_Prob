# https://velog.io/@hyuntall/%EB%B0%B1%EC%A4%80-2579%EB%B2%88-%EA%B3%84%EB%8B%A8-%EC%98%A4%EB%A5%B4%EA%B8%B0-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
DP = [0]*(N+1)
point = [0]+[int(input()) for _ in range(N)]

DP[1] = point[1]

if N>=2:
    DP[2] = point[1]+point[2]
if N>=3:
    DP[3] = point[3] + max(point[1], point[2])

if N>=4:
    for i in range(4, N+1):
        DP[i] = max(DP[i-3]+point[i-1]+point[i], DP[i-2]+point[i])
print(DP[N])
print(DP)
# [0, 10, 30, 35, 55, 65, 75]
