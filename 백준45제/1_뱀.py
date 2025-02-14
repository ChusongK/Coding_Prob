import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def in_range(ni, nj):
    return 0<=ni<N and 0<=nj<N

N = int(input())
K = int(input())
apple = []
for _ in range(K):
    a, b = map(int,input().split())
    apple.append((a-1,b-1))
L = int(input())
order = dict()
for _ in range(L):
    T, D = input().split()
    order[int(T)] = D

t = 0
q = deque([(0,0)])
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d = 1

while True:
    t += 1
    ci, cj = q[-1]
    ni, nj = ci+dir[d][0], cj+dir[d][1]
    if not in_range(ni, nj) or (ni, nj) in q:
        break
    q.append((ni, nj))
    if (ni, nj) in apple:
        apple.remove((ni, nj))
    else:
        q.popleft()
    if t in order.keys():
        if order[t]=='L':
            d = (d-1)%4
        else:
            d = (d+1)%4
print(t)