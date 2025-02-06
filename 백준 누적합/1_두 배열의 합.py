import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

dict_A = {}
dict_B = {}

for i in range(N):
    for j in range(i, N):
        total = sum(A[i:j+1])
        if total in dict_A.keys():
            dict_A[total]+=1
        else:
            dict_A[total] = 1
for i in range(M):
    for j in range(i, M):
        total = sum(B[i:j+1])
        if total in dict_B.keys():
            dict_B[total]+=1
        else:
            dict_B[total] = 1

cnt = 0
for a in dict_A.keys():
    if T-a in dict_B.keys():
        cnt += dict_A[a]*dict_B[T-a]
print(cnt)