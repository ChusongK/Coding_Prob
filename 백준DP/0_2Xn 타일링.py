import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

DP = [0]*1001

DP[1]=1
DP[2]=2
DP[3]=3

for i in range(4, N+1):
    DP[i] = DP[i-1] + DP[i-2]
print(DP[N]%10007)