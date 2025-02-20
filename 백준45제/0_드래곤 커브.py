import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [[0]*101 for _ in range(101)]

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
for _ in range(N):      # 드래곤커브 개수만큼 입력 받기
    sj, si, dr, g = map(int, input().split())
    lst = [(si,sj)]     # 시작위치 저장
    lst.append((si+di[dr], sj+dj[dr]))  # 0세대 위치 저장
    for _ in range(g):  # 세대 회수만큼 뻗음
        # lst의 끝 좌표 기준으로 90도 회전
        ei, ej = lst[-1]
        for i in range(len(lst)-2, -1, -1):
            ci, cj = lst[i]
            lst.append((ei-(ej-cj), ej+(ei-ci)))

    # arr에 드래곤 커브 표시
    for i, j in lst:
        arr[i][j] = 1

ans = 0
# 2*2 네칸이 모두 1인 경우 찾기
for i in range(100):
    for j in range(100):
        if arr[i][j]==arr[i][j+1]==arr[i+1][j]==arr[i+1][j+1]==1:
            ans += 1
print(ans)