import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

# !!! 문제 조건을 잘보자... 가능한 값 범위를 벗어나는지 체크하는 조건문 추가해야했음.
# 방문표시를 처음에 안했음.

N, K = map(int, input().split())
MAX = 10**5

def bfs(N, K):
    global MAX

    q = deque()
    q.append(N)
    v = [0]*(MAX+1)
    v[N] = 1
    while q:
        n = q.popleft()
        if n==K:
            print(v[n]-1)
            break
        for i in (n-1, n+1, 2*n):
            if 0<=i<=MAX and not v[i]:    # 아직 미방문이면,
                v[i] = v[n] + 1
                q.append(i)

bfs(N, K)