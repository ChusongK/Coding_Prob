import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(id, d):
    global dir
    q = deque()
    q.append(id)
    dir[id] = d
    v = [0]*5
    v[id] = 1

    while q:
        cur_id = q.popleft()
        for dist in (-1, 1):
            nxt_id = cur_id + dist
            if 1<=nxt_id<=4 and not v[nxt_id]:
                q.append(nxt_id)
                v[nxt_id] = 1
                if dir[cur_id]!=0:
                    if (cur_id<nxt_id and
                        arr[cur_id-1][2]!=
                                arr[nxt_id-1][6])\
                            or \
                        (cur_id>nxt_id and
                         arr[nxt_id-1][2]!=
                         arr[cur_id-1][6]):
                            dir[nxt_id] = dir[cur_id]*(-1)

arr = []
for _ in range(4):
    q = deque(map(int, input().strip()))
    arr.append(q)
K = int(input())
rot = [tuple(map(int, input().split())) for _ in range(K)]

for i in range(K):
    dir = [0] * 5
    # 현재 회전
    cur_id, cur_d = rot[i]
    # 바퀴별 회전 방향 저장
    bfs(cur_id, cur_d)

    # 회전 반영
    for i in range(1,5):
        if dir[i]==0:
            continue
        q = arr[i-1]
        # 시계 회전
        if dir[i]==1:
            q.appendleft(q.pop())
        # 반시계 회전
        else:
            q.append(q.popleft())
        # 회전결과 업데이트
        arr[i-1] = q

sm = 0
for i in range(4):
    if arr[i][0]==0:
        continue
    else:
        sm += 2**i
print(sm)