import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))
ans = 0

start = 0
end = max(trees)

while start<=end:
    mid = (start+end)//2
    total = 0

    for tree in trees:
        if tree>mid:
            total += tree-mid
    if total>=M:
        ans = mid
        start = mid+1
    else:
        end = mid-1
print(ans)
