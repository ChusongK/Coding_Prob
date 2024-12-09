import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M, V = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    arr[x][y] = arr[y][x] = 1

v = [0]*(N+1)

def dfs(V):
    print(V, end=' ')
    v[V] = 1

    for i in range(1, N+1):
        if arr[V][i]==1 and not v[i]:
            dfs(i)


def bfs(V):
    q = deque()
    q.append(V)
    v[V] = 1

    while q:
        now = q.popleft()
        print(now, end= ' ')
        for i in range(1, N+1):
            if arr[now][i]==1 and not v[i]:
                q.append(i)
                v[i] = 1

dfs(V)
print()
v = [0]*(N+1)

bfs(V)

# for i in arr:
#     print(i)
# print(N)