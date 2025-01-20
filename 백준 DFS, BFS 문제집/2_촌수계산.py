import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N = int(input())
X, Y = map(int, input().split())
M = int(input())

graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def bfs(X):
    v = [0]*(N+1)
    v[X] = 1
    q = deque()
    q.append(X)

    while q:
        n = q.popleft()
        if n==Y:
            print(v[n]-1)
            exit(0)
        for i in range(1, N+1):
            if not v[i] and graph[n][i]==1:
                q.append(i)
                v[i] = v[n] + 1
    print(-1)
bfs(X)