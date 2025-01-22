import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N = int(input())
K = int(input())
apples = set()
for _ in range(K):
    a, b = map(int, input().split())
    apples.add((a-1, b-1))
orders = dict()
L = int(input())
for _ in range(L):
    a, b = input().split()
    orders[int(a)] = b

snake = deque()
snake.append((0,0))
# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
d = 1   # 초기 우

def in_range(x, y):
    return 0<=x<N and 0<=y<N

t = 0
while True:
    t += 1

    # 머리 참조
    ci, cj = snake[-1]
    # 머리 늘려서 한칸 움직임 시도
    ni, nj = ci+dx[d], cj +dy[d]
    # 벽이나 자기자신과 안 부딪혔다면, 움직임 반영
    if in_range(ni, nj) and (ni, nj) not in snake:
        snake.append((ni, nj))
    else:   # 시간 출력하고 게임종료
        print(t)
        exit(0)
    # 움직인 자리에 사과 있으면, 먹기
    if (ni, nj) in apples:
        apples.remove((ni, nj))
    else:   # 사과 없으면 꼬리 자르기
        snake.popleft()
    # 방향 변환 할게 있으면 변환
    if t in orders.keys():
        if orders[t]=='D':
            d = (d+1)%4
        else:
            d = (d-1)%4
