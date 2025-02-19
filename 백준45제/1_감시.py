import sys
sys.stdin = open('input.txt', 'r')

def cal(tlst):
    v = [[0]*(M+2) for _ in range(N+2)]
    for i in range(CNT):
        ci, cj = lst[i]
        r = tlst[i]
        type = arr[ci][cj]
        for dr in tv[type]:
            dr = (dr+r)%4
            ni, nj = ci, cj
            while True:
                ni, nj = ni+di[dr], nj+dj[dr]
                if arr[ni][nj]==6:
                    break
                v[ni][nj] = 1
    cnt = 0
    for i in range(1,N+1):
        for j in range(1, M+1):
            if arr[i][j]==0 and v[i][j]==0:
                cnt += 1
    return cnt

def dfs(n, tlst):
    global ans
    if n==CNT:
        ans = min(ans, cal(tlst))
        return
    dfs(n+1, tlst+[0])
    dfs(n+1, tlst+[1])
    dfs(n+1, tlst+[2])
    dfs(n+1, tlst+[3])

N, M = map(int, input().split())
arr = [[6]*(M+2)]+[[6]+list(map(int, input().split()))+[6] for _ in range(N)]+[[6]*(M+2)]
lst = [(i, j) for i in range(1,N+1) for j in range(1,M+1) if 1<=arr[i][j]<=5]
CNT = len(lst)
tv = [[], [1], [1,3], [0,1], [0,1,3], [0,1,2,3]]
ans = N*M
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
dfs(0, [])
print(ans)