# import sys
# sys.stdin = open('input.txt', 'r')
from collections import deque

N, K = map(int, input().split())

def bfs(N, K):
    q = deque()
    q.append((N, 0))

    while q:
        n, cnt = q.popleft()
        if n==K:
            print(cnt)
            break
        q.append((n - 1, cnt + 1))
        q.append((n + 1, cnt + 1))
        q.append((2 * n, cnt + 1))
bfs(N, K)