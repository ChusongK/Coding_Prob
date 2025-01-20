import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

F, S, G, U, D = map(int, input().split())

v = [0]*(F+1)

def bfs():
    v[S] = 1
    q = deque()
    q.append(S)

    while q:
        n = q.popleft()
        if n==G:
            print(v[n]-1)
            exit(0)
        for i in (n+U, n-D):
            if 1<=i<=F and not v[i]:
                q.append(i)
                v[i] = v[n] + 1
    print("use the stairs")

bfs()