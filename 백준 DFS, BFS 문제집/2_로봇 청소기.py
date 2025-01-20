"""
현재칸 주변 4칸 중 청소 안된 칸이 있으면
반시계 90 회전인줄 알았는데
90도씩 반시계로 돌면서 주변 4칸 중 청소안된 칸 있는지 찾는거였음.
찾으면 바로 전진하고 1번으로 돌아가는거고.
"""

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M = map(int, input().split())
R, C, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 북동남서
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cnt = 0

while True:
    if arr[R][C]==0:
        cnt += 1
        arr[R][C] = -1

    for _ in range(4):
        D = (D - 1) % 4
        if arr[R+directions[D][0]][C+directions[D][1]]==0:
            R, C = R+directions[D][0], C+directions[D][1]
            break
    else:
        if arr[R+directions[(D+2)%4][0]][C+directions[(D+2)%4][1]]!=1:
            R, C = R+directions[(D+2)%4][0], C+directions[(D+2)%4][1]
        else:
            print(cnt)
            exit(0)
