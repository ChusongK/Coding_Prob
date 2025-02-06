# https://codinghejow.tistory.com/246
import sys
sys.stdin = open('input.txt', 'r')
import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
sum_ = arr[0]
ans = sys.maxsize

while True:
    if sum_ < S:
        end += 1
        if end == N: break
        sum_ += arr[end]
    else:
        sum_ -= arr[start]
        ans = min(ans, end - start + 1)
        start += 1

print(ans if ans != sys.maxsize else 0)