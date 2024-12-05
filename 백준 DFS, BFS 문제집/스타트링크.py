import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

# 문제 조건을 꼼꼼히 보자, D는 내려가니까 - 붙여서 더해야함.
F, S, G, U, D = map(int, input().split())

def bfs():
    q = deque()
    q.append(S)
    v = [0]*(F+1)
    v[S] = 1

    while q:
        cur = q.popleft()
        print("pop: ", cur)
        if cur==G:
            print(v[cur]-1)
            exit(0)
        for i in (U, -D):
            next = cur + i
            if 1<=next<=F and v[next]==0:
                q.append(next)
                v[next] = v[cur] + 1
                # print(v)
                # print(q)
    print("use the stairs")
bfs()