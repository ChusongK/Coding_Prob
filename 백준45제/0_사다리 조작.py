import sys
sys.stdin = open('input.txt', 'r')

def check():
    for j in range(1, N+1):
        cj = j
        for i in range(1, H+1):
            if arr[i][cj]==1:
                cj += 1
            elif arr[i][cj-1]==1:
                cj -= 1
        # print(j, cj)
        if j!=cj:
            return False
    return True

def dfs(n, s):
    global res
    if res==True:
        return
    if n==cnt:
        # print(cnt)
        # for i in arr:
        #     print(i)
        if check():
            res = True
        return
    for i in range(s, CNT):
        ci, cj = pos[i]
        if arr[ci][cj-1]!=1 and arr[ci][cj+1]!=1:
            arr[ci][cj] = 1
            dfs(n+1, i+1)
            arr[ci][cj] = 0

N, M, H = map(int, input().split())
arr = [[0]*(N+2) for _ in range(H+1)]
for _ in range(M):
    i, j = map(int, input().split())
    arr[i][j] = 1
pos = [(i, j) for i in range(1, H+1) for j in range(1, N+1) \
       if arr[i][j]==0 and arr[i][j-1]==0 and arr[i][j+1]==0]
CNT = len(pos)
ans = 0
res = False

for cnt in range(4):
    dfs(0, 0)
    if res:
        ans = cnt
        break
else:
    ans = -1
print(ans)