import sys
sys.stdin = open('input.txt', 'r')

N, K =map(int, input().split())
num = list(map(int, input().split()))

cum = [0]*(N+1)
total = 0
for i in range(N):
    total += num[i]
    cum[i+1] = total

diffs = []
lt = 0
rt = K
while rt<=N:
    diffs.append(cum[rt]-cum[lt])
    lt += 1
    rt += 1
print(max(diffs))