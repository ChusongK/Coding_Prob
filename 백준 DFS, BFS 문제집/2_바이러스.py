import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N = int(input())
M = int(input())
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

def bfs():
    v = [0]*(N+1)
    v[1] = 1    # 방문 표시
    q = deque()
    q.append(1)
    cnt = 0
    while q:
        n = q.popleft()
        for i in range(1, N+1):
            if not v[i] and graph[n][i]==1:
                q.append(i)
                v[i] = 1
                cnt += 1
    print(cnt)
bfs()
