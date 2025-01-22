import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def move(arr):  # 행단위로 이동(같은값 합치기)시키는 함수
    for i in range(len(arr)):       # 행 개수만큼 처리
        num = 0                     # app 해야할 기준숫자(같으면 두배로)
        tlst = []
        for n in arr[i]:        # 행에서 숫자 하나씩 처리
            if n==0:    continue    # 빈칸은 당연히 처리 안함
            if n==num:          # 기준숫자와 같은경우(합침!)
                tlst.append(num*2)
                num = 0
            else:               # 기준숫자와 다른경우
                if num==0:      # 처음 숫자를 만난경우
                    num=n
                else:
                    tlst.append(num)
                    num=n
        # 종료후 기준숫자 있으면 tlst추가 그리고 남은 자리 0으로 채움
        if num>0:           # 마지막에 숫차 추가
            tlst.append(num)
        # tlst 남은 길이를 0으로 채움
        arr[i] = tlst+[0]*(N-len(tlst))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def dfs(n, arr):
    global ans
    # [1] 종료조건: 5번 처리 완료
    if n==5:
        ans = max(ans, max(map(max, arr)))  # arr 중 가장 큰 값
        return

    # 좌측이동(좌측으로 기울이기): 기준
    narr = [x[:] for x in arr]  # 딥카피해서 전달
    move(narr)
    dfs(n+1, narr)

    narr = [x[::-1] for x in arr]  # 우측
    move(narr)
    dfs(n+1, narr)

    arr_t = list(map(list, zip(*arr)))  # 열=>행으로 처리
    narr = [x[:] for x in arr_t]        # 상방향: 딥카피하기
    move(narr)
    dfs(n+1, narr)

    narr = [x[::-1] for x in arr_t]     # 하방향: 딥카피하기
    move(narr)
    dfs(n+1, narr)

# 상하좌우 네방향(가능한 모든경우 처리)
ans = 0
dfs(0, arr)
print(ans)