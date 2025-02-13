# 1. 인덱스 처리
# 첫 번째 코드에서는 배열 인덱스를 직접 사용하고 있습니다. 즉, arr[a][b]와 같은 방식으로 a와 b 값을 그대로 사용합니다.
# 두 번째 코드에서는 a, b 값을 각각 1씩 감소시켜서 arr[a-1][b-1]을 사용합니다. 이는 배열 인덱스를 0부터 시작하는 Python의 인덱스와 1부터 시작하는 문제의 요구 사항을 맞추기 위한 처리가 필요하기 때문입니다.

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
mn = float('inf')

def cal(t1, t2):
    sm1 = sm2 = 0

    for i in range(len(t1)-1):
        for j in range(i+1, len(t1)):
            a, b = t1[i], t1[j]
            sm1 += arr[a][b]
            sm1 += arr[b][a]

    for i in range(len(t2)-1):
        for j in range(i+1, len(t2)):
            a, b = t2[i], t2[j]
            sm2 += arr[a][b]
            sm2 += arr[b][a]

    return abs(sm1-sm2)

def dfs(n, t1, t2):
    global mn

    if len(t1)>N//2 or len(t2)>N//2:
        return
    if mn==0:
        print(mn)
        exit(0)
    if n==N:
        mn = min(mn, cal(t1, t2))
        return

    dfs(n+1, t1+[n], t2)
    dfs(n+1, t1, t2+[n])

dfs(0, [], [])
print(mn)