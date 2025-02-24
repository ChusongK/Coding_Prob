import sys
sys.stdin = open('input.txt', 'r')

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
fixed = False
for i in range(R):
    if arr[i][0]==-1 and not fixed:
        rob_u = i
        fixed = True
    elif arr[i][0]==-1 and fixed:
        rob_d = i
        break

for _ in range(T):
    narr = [x[:] for x in arr]
    for i in range(R):
        for j in range(C):
            if arr[i][j]>0:
                cnt = 0
                for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni,nj = i+di, j+dj
                    if 0<=ni<R and 0<=nj<C and arr[ni][nj]!=-1:
                        narr[ni][nj] += arr[i][j]//5
                        cnt += 1
                narr[i][j] -= (arr[i][j]//5*cnt)
    arr = narr

    for i in range(rob_u-1, 0, -1):
        arr[i][0] = arr[i-1][0]
    arr[0][:C-1] = arr[0][1:]
    for i in range(rob_u):
        arr[i][C-1] = arr[i+1][C-1]
    arr[rob_u][2:] = arr[rob_u][1:C-1]
    arr[rob_u][1] = 0

    for i in range(rob_d+1, R-1):
        arr[i][0] = arr[i+1][0]
    arr[R-1][:C-1] = arr[R-1][1:]
    for i in range(R-1, rob_d, -1):
        arr[i][C-1] = arr[i-1][C-1]
    arr[rob_d][2:] = arr[rob_d][1:C-1]
    arr[rob_d][1] = 0

print(sum(map(sum, arr)) + 2)
