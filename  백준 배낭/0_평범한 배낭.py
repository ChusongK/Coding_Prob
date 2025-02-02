# https://hongcoding.tistory.com/50
import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(N)]
arr = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    w, v = lst[i-1]
    for j in range(1, K+1):
        if j<w:
            arr[i][j] = arr[i-1][j]
        else:
            arr[i][j] = max(arr[i-1][j-w] + v, arr[i-1][j])

print(arr[N][K])