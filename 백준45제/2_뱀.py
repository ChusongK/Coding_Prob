import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def in_range(ni, nj):
    return 0<=ni<N and 0<=nj<N

N = int(input())
K = int(input())
apple = []
for _ in range(K):
    a, b = map(int, input().split())
    apple.append((a-1, b-1))
L = int(input())
order = dict()
for _ in range(L):
    sec, dir = input().split()
    order[int(sec)] = dir
d = 1
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
time = 0
q = deque()
q.append((0,0))

while True:
    time += 1

    ci, cj = q[-1]
    ni, nj = ci+di[d], cj+dj[d]

    if not in_range(ni, nj) or (ni, nj) in q:
        break
    q.append((ni, nj))
    if (ni, nj) in apple:
        apple.remove((ni, nj))
    else:
        q.popleft()
    if time in order.keys():
        if order[time]=='L':
            d = (d-1)%4
        else:
            d = (d+1)%4
print(time)



