import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

t = int(input())

def bfs():
    q = deque()
    v = [0]*(n+1)
    q.append((si, sj))

    while q:
        ci, cj = q.popleft()
        dist_to_end = abs(ei - ci) + abs(ej - cj)
        if dist_to_end<=1000: # 목적지 갈 수 있으면,
            print("happy")
            return
        for i in range(n):
            ni, nj = stores[i]
            dist = abs(ni - ci) + abs(nj - cj)
            if v[i+1]==0 and dist<=1000:    # 미방문, 갈 수 있으면,
                q.append((ni, nj))
                v[i+1] = 1
    print("sad")


for _ in range(t):
    n = int(input())
    si, sj = map(int, input().split())

    stores = []

    for _ in range(n):
        x, y = map(int, input().split())
        stores.append((x, y))

    ei, ej = map(int, input().split())
    bfs()



