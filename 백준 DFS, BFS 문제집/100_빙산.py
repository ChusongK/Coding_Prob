import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 빙산 위치만 관리
ice_positions = {(i, j) for i in range(1, N - 1) for j in range(1, M - 1) if arr[i][j] > 0}

# 상하좌우 탐색
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def melt_ice(positions):
    """빙산 녹이기"""
    to_melt = []
    for x, y in positions:
        sea_count = sum(1 for dx, dy in directions if arr[x + dx][y + dy] == 0)
        to_melt.append((x, y, sea_count))

    # 녹인 결과 반영
    new_positions = set()
    for x, y, sea_count in to_melt:
        arr[x][y] = max(0, arr[x][y] - sea_count)
        if arr[x][y] > 0:
            new_positions.add((x, y))
    return new_positions


def bfs(start, visited):
    """빙산 연결성 확인"""
    q = deque([start])
    visited.add(start)

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) in ice_positions and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))


def count_icebergs():
    """빙산 덩어리 개수 세기"""
    visited = set()
    count = 0
    for position in ice_positions:
        if position not in visited:
            bfs(position, visited)
            count += 1
    return count


time = 0
while ice_positions:
    time += 1
    ice_positions = melt_ice(ice_positions)

    if not ice_positions:  # 빙산이 모두 녹음
        print(0)
        break
    if count_icebergs() >= 2:  # 빙산이 분리됨
        print(time)
        break