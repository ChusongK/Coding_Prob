import sys
sys.stdin = open('input.txt', 'r')
import sys

N, S = map(int, input().split())
nums = list(map(int, input().split()))

total = nums[0]
start = end = 0
ans = sys.maxsize

while True:
    if total<S:
        end += 1
        if end==N:  break
        total += nums[end]
    else:
        total -= nums[start]
        ans = min(ans, end-start+1)
        start += 1

print(ans if ans!=sys.maxsize else 0)

