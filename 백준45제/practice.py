import sys

sys.stdin = open('input.txt', 'r')




N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = float('-inf')
narr = list(map(list, zip(*arr)))
for i in arr:
    print(i)
