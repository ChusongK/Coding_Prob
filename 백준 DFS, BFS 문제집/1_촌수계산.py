import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N = int(input())
a, b = map(int, input().split())
M = int(input())

arr = [[0]*(N+1) for _ in range(N+1)]
v = [0]*(N+1)

for _ in range(M):
    x, y = map(int, input().split())
    arr[x][y] = arr[y][x] = 1

def bfs(a, b):
    q = deque()
    q.append(a)
    v[a] = 1

    while q:
        now = q.popleft()
        if now==b:
            print(v[now]-1)
            exit(0)
        for i in range(1, N+1):
            if arr[now][i]==1 and v[i]==0:
                q.append(i)
                v[i] = v[now] + 1
    print(-1)

bfs(a, b)