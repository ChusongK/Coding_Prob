import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
a, b = map(int, input().split())
M = int(input())

graph = [[0]*(N+1) for _ in range(N+1)]
v = [0]*(N+1)

for _ in range(M):
    f, s = map(int, input().split())
    graph[f][s] = graph[s][f] = 1

def bfs(a, b):
    q = [a]
    v[a] = 1
    is_found = False
    # cnt = 0

    while q:
        now = q.pop(0)
        if now==b:
            print(v[now] - 1)
            is_found = True
            break
        for i in range(1, N+1):
            if not v[i] and graph[now][i]:
                q.append(i)
                v[i] = v[now] + 1

    if not is_found:    print(-1)

bfs(a, b)

# for i in graph:
#     print(i)