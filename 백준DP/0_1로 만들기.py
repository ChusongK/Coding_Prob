# https://jominseoo.tistory.com/98
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
DP = [0]*(int(10e6)+1)

for i in range(2, N+1):
    DP[i] = DP[i-1]+1
    if i%2==0:
        DP[i] = min(DP[i//2]+1, DP[i])
    if i%3==0:
        DP[i] = min(DP[i//3]+1, DP[i])

print(DP[N])