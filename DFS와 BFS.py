# 블로그 링크
# https://velog.io/@falling_star3/2.-%EA%B9%8A%EC%9D%B4%EC%9A%B0%EC%84%A0%ED%83%90%EC%83%89DFS%EA%B3%BC-%EB%84%93%EC%9D%B4%EC%9A%B0%EC%84%A0%ED%83%90%EC%83%89BFS
import sys
sys.stdin = open("input.txt", "r")

N, M, V = map(int, input().split())

# 행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# 방문 리스트 행렬
visited1 = [0]*(N+1)
visited2 = visited1.copy()

# dfs 함수 만들기
def dfs(V):
    visited1[V] = 1 # 방문처리
    print(V, end = ' ')
    for i in range(1, N+1):
        if graph[V][i] and not visited1[i]:
            dfs(i)

def dfs(V):
    visited1[V] = 1
    print(V, end = ' ')
    for i in range(0, N+1):
        if graph[V][i] and not visited1[i]:
            dfs(i)

def bfs(V):
    queue = [V]
    visited2[V] = 1 # 방문처리
    while queue:
        V = queue.pop(0) # 방문 노드 제거
        print(V, end = ' ')
        for i in range(1, N+1):
            if not visited2[i] and graph[V][i]:
                queue.append(i)
                visited2[i] = 1
dfs(V)
print()
bfs(V)

