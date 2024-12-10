import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N = int(input())
M = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]
v = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1

def bfs():
    q = deque()
    q.append(1)
    v[1] = 1
    cnt = 0

    while q:
        now = q.popleft()
        for i in range(1, N+1):
            if arr[now][i]==1 and v[i]==0:
                q.append(i)
                v[i] = 1
                cnt += 1
    print(cnt)

bfs()