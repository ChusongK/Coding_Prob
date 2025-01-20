import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M, V = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    X, Y = map(int, input().split())
    graph[X][Y] = graph[Y][X] = 1

def dfs(V):
    v[V] = 1    # 방문 표시
    print(V, end=' ')

    for i in range(1, N+1):
        if graph[V][i]==1 and not v[i]:
            dfs(i)

v = [0]*(N+1)
dfs(V)

print()

def bfs(V):
    v[V] = 1    # 방문 표시
    q = deque()
    q.append(V)

    while q:
        n = q.popleft()
        print(n, end=' ')
        for i in range(1, N+1):
            if graph[n][i]==1 and not v[i]:
                q.append(i)
                v[i] = 1

v = [0]*(N+1)
bfs(V)