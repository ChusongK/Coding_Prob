# https://khsung0.tistory.com/44
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
cnt += N

for i in range(N):
    A[i] = max(A[i]-B, 0)

for i in range(N):
    if A[i]%C!=0:
        cnt += A[i]//C+1
    else:
        cnt += A[i]//C
print(cnt)