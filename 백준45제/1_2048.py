import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 2

def move(arr):
    for i in range(len(arr)):
        num = 0
        tlst = []
        for n in arr[i]:
            if n==0:    continue
            if n==num:
                tlst.append(num*2)
                num=0
            else:
                if num==0:
                    num=n
                else:
                    tlst.append(num)
                    num=n
        if num>0:
            tlst.append(num)
        arr[i] = tlst + [0]*(N-len(tlst))

def dfs(n, arr):
    global ans
    if n==5:
        ans = max(ans, max(map(max, arr)))
        return

    narr = [x[:] for x in arr]
    move(narr)
    dfs(n+1, narr)

    narr = [x[::-1] for x in arr]
    move(narr)
    dfs(n+1, narr)

    arr_t = list(map(list, zip(*arr)))

    narr = [x[:] for x in arr_t]
    move(narr)
    dfs(n+1, narr)

    narr = [x[::-1] for x in arr_t]
    move(narr)
    dfs(n+1, narr)

dfs(0, arr)
print(ans)