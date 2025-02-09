# https://hongcoding.tistory.com/128
import sys
sys.stdin = open('input.txt', 'r')

N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))
dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]

dice = dict()
for i in range(1, 7):
    dice[i] = 0

def in_range(nx, ny):
    return 0<=nx<N and 0<=ny<M

def move(d):
    if d==1:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]
    elif d==2:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]
    elif d==3:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]
    elif d==4:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]

for d in orders:
    nx, ny = x+dir[d-1][0], y+dir[d-1][1]
    if not in_range(nx, ny):
        continue
    x, y = nx, ny

    move(d)
    print(dice[1])

    if arr[x][y]==0:
        arr[x][y] = dice[6]
    else:
        dice[6] = arr[x][y]
        arr[x][y] = 0