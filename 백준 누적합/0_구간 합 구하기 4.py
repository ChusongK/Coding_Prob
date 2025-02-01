import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
cum = [0]
tmp = 0

for i in range(N):
    tmp += num[i]
    cum.append(tmp)

for _ in range(M):
    i, j = map(int, input().split())
    print(cum[j] - cum[i-1])