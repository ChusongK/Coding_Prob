import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

T = int(input())

def bfs():
    q = deque()
    q.append((si, sj))
    v = set()

    while q:
        ci, cj = q.popleft()
        dist1 = abs(ei-ci)+abs(ej-cj)
        if dist1<=1000:
            print("happy")
            return

        for (i, j) in stores_set:
            dist2 = abs(i-ci)+abs(j-cj)
            if dist2<=1000 and (i, j) not in v:
                q.append((i, j))
                v.add((i, j))
    print("sad")

for test_case in range(T):
    N = int(input())
    si, sj = map(int, input().split())

    stores_set = set()
    for conv_store in range(N):
        x, y = map(int, input().split())
        stores_set.add((x, y))

    ei, ej = map(int, input().split())

    bfs()