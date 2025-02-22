import sys
sys.stdin = open('input.txt', 'r')

def dist(tlst):
    total = 0
    for i, j in home:
        tmp = float('inf')
        for now in tlst:
            ci, cj = chick[now]
            d = abs(ci-i)+abs(cj-j)
            tmp = min(d, tmp)
        total += tmp
    return total

def dfs(n, s, tlst):
    global ans
    if n==m:
        ans = min(ans, dist(tlst))
        return
    for i in range(s, CNT):
        dfs(n+1, i+1, tlst+[i])

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chick = [(i, j) for i in range(N) for j in range(N) if arr[i][j]==2]
home = [(i, j) for i in range(N) for j in range(N) if arr[i][j]==1]
CNT = len(chick)
ans = float('inf')

for m in range(1, M+1):
    dfs(0, 0, [])
print(ans)