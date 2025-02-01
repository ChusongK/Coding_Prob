import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M = map(int, input().split())

cnt = 0
lst = deque()
total = 0

for i in map(int, input().split()):
    total += i
    lst.append(i)

    while True:
        if total==M:
            cnt += 1
            break
        elif total>M:
            total -= lst.popleft()
        else:
            break
print(cnt)