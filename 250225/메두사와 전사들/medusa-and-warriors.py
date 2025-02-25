import sys
from collections import deque
import copy

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def see(d):
    q = deque([(ai, aj)])
    s = set()
    visited = set()
    
    while q:
        i, j = q.popleft()
        if (i, j) in visited:
            continue
        visited.add((i, j))
        s.add((i, j))
        
        ni, nj = i + di[d], j + dj[d]
        if in_range(ni, nj) and grid[ni][nj] != 1:
            q.append((ni, nj))
    return s

def search():
    q = deque([(ai, aj, 0)])
    visited = set([(ai, aj)])
    
    while q:
        i, j, dist = q.popleft()
        if (i, j) == (bi, bj):
            return dist
        
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if in_range(ni, nj) and (ni, nj) not in visited and grid[ni][nj] != 1:
                visited.add((ni, nj))
                q.append((ni, nj, dist + 1))
    return -1

N, M = map(int, sys.stdin.readline().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, sys.stdin.readline().split())))

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

temp = list(map(int, sys.stdin.readline().split()))
ai, aj, bi, bj = temp[:4]
war = temp[4:]

distance = search()
if distance == -1:
    print(-1)
    exit()

while True:
    new_war = copy.deepcopy(war)
    for i in range(M):
        wi, wj = war[2*i], war[2*i+1]
        if in_range(wi, wj):
            for d in range(4):
                ni, nj = wi + di[d], wj + dj[d]
                if in_range(ni, nj) and grid[ni][nj] == 0:
                    new_war[2*i], new_war[2*i+1] = ni, nj
                    break
    
    if new_war == war:
        break
    war = new_war
    
    distance = search()
    if distance == -1:
        print(-1)
        exit()

print(distance)
