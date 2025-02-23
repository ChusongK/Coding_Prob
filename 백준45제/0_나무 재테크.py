import sys
sys.stdin = open('input.txt', 'r')

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
arr = [[[] for _ in range(N)] for _ in range(N)]
food = [[5]*N for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    arr[x-1][y-1].append(z)

for _ in range(K):
    dead = []
    breed = []
    for i in range(N):
        for j in range(N):
            arr[i][j].sort()
            tmp = []
            for e in arr[i][j]:
                if food[i][j]<e:
                    dead.append((i, j, e))
                else:
                    food[i][j] -= e
                    tmp.append(e+1)
                    if (e+1)%5==0:
                        breed.append((i, j))
            arr[i][j] = tmp
    for i, j, a in dead:
        food[i][j] += a//2
    for i, j in breed:
        for di,dj in ((-1,-1), (-1,0), (-1,1), (0,-1),(0,1),(1,-1),(1,0),(1,1)):
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N:
                arr[ni][nj].append(1)
    for i in range(N):
        for j in range(N):
            food[i][j] += A[i][j]

cnt = 0
for i in range(N):
    for j in range(N):
        cnt += len(arr[i][j])
print(cnt)