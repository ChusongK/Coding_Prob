# https://dreamtreeits.tistory.com/21
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
N = int(input())
lst_a = list(map(int, input().split()))
M = int(input())
lst_b = list(map(int, input().split()))

A = dict()
B = dict()

for i in range(N):
    for j in range(i, N):
        sm_a = sum(lst_a[i:j+1])
        if sm_a in A.keys():
            A[sm_a] += 1
        else:
            A[sm_a] = 1

for i in range(M):
    for j in range(i, M):
        sm_b = sum(lst_b[i:j+1])
        if sm_b in B.keys():
            B[sm_b] += 1
        else:
            B[sm_b] = 1

cnt = 0
for i in A.keys():
    if T-i in B.keys():
        cnt += A[i]*B[T-i]
print(cnt)