import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, K = map(int, input().split())

v = [0]*100001

def bfs(N):
    v[N] = 1
    q = deque()
    q.append(N)

    while q:
        n = q.popleft()
        if n==K:
            print(v[n]-1)
            exit(0)
        for i in (n-1, n+1, 2*n):
            if 0<=i<=100000 and not v[i]:
                q.append(i)
                v[i] = v[n] + 1

bfs(N)