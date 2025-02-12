import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
mn = float('inf')

def cal(one, two):
    sm_1 = 0
    sm_2 = 0
    for i in range(len(one)-1):
        for j in range(i+1, len(one)):
            a, b = one[i], one[j]
            sm_1 += arr[a][b]
            sm_1 += arr[b][a]
    for i in range(len(two)-1):
        for j in range(i+1, len(two)):
            a, b = two[i], two[j]
            sm_2 += arr[a][b]
            sm_2 += arr[b][a]

    return abs(sm_1 - sm_2)

def dfs(n, one, two):
    global mn
    if len(one)>N//2 or len(two)>N//2:
        return
    if n==N:
        res = cal(one, two)
        mn = min(mn, res)
        return

    dfs(n+1, one+[n], two)
    dfs(n+1, one, two+[n])


dfs(0, [], [])
print(mn)