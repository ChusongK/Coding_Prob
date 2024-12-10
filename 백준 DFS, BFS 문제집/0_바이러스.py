import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
K = int(input())
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(K):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

v = [0]*(N+1)

def bfs():
    q = [1]
    v[1] = 1
    cnt = 0

    while q:
        cur = q.pop(0)
        for new in range(1, N+1):
            if not v[new] and graph[cur][new]:
                q.append(new)
                v[new] = 1
                cnt += 1
    print(cnt)

bfs()

# for i in graph:
#     print(i)
