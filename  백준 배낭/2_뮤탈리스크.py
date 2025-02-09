import sys
from collections import deque
from itertools import permutations
# sys.stdin = open('input.txt', 'r')

N = int(input())
hp = list(map(int, input().split()))
hp += [0]*(3-N)

visited = [[[0]*61 for i in range(61)] for j in range(61)]

visited[hp[0]][hp[1]][hp[2]] = 1
q = deque()
q.append(hp)

while q:
    ci, cj, ck = q.popleft()
    if (ci, cj, ck)==(0,0,0):
        print(visited[ci][cj][ck]-1)
        break
    for ai, aj, ak in permutations([9, 3, 1], 3):
        ni, nj, nk = max(ci-ai, 0), max(cj-aj, 0), max(ck-ak, 0)
        if visited[ni][nj][nk]==0:
            q.append([ni, nj, nk])
            visited[ni][nj][nk] = visited[ci][cj][ck]+1
