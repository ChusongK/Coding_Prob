"""
편의점 방문표시하는 v = set() 을 안 만들고 체크 안하니
무한루프 돈다. 이유는 이미 추가된 편의점 좌표가 계속
q에 들어가니까.
"""

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
        if abs(ei-ci)+abs(ej-cj)<=1000:
            print('happy')
            return
        for i, j in stores:
            if abs(i-ci)+abs(j-cj)<=1000 and (i, j) not in v:
                q.append((i, j))
                v.add((i, j))
    print('sad')

for _ in range(T):
    N = int(input())    # 편의점 수
    si, sj = map(int, input().split())
    stores = set()
    for _ in range(N):
        x, y = map(int, input().split())
        stores.add((x,y))
    ei, ej = map(int, input().split())
    bfs()
