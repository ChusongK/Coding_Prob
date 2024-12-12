import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

F, S, G, U, D = map(int, input().split())
v = [0]*(F+1)

def bfs():
    q = deque()
    q.append(S)
    v[S] = 1

    while q:
        now = q.popleft()
        if now==G:
            print(v[now]-1)
            exit(0)
        for i in (now + U, now - D):
            if 1<=i<=F and v[i]==0:
                q.append(i)
                v[i] = v[now] + 1
    print("use the stairs")

bfs()