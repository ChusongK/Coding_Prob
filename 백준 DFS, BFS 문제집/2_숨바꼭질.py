import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M = map(int, input().split())
v = [0]*100001

def bfs():
    q = deque()
    q.append(N)
    v[N] = 1

    while q:
        now = q.popleft()
        if now==M:
            print(v[now]-1)
            break
        for i in (now-1, now+1, now*2):
            if 0<=i<=100000 and v[i]==0:
                q.append(i)
                v[i] = v[now] + 1

bfs()
