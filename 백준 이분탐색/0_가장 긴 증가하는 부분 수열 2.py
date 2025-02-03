# https://onn5.tistory.com/36
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
A = list(map(int, input().split()))
LIS = [0]

def binary_search(e):
    start = 0
    end = len(LIS)-1
    while start<=end:
        mid = (start+end)//2
        if LIS[mid]==e:
            return mid
        elif LIS[mid]<e:
            start = mid+1
        else:
            end = mid-1
    return start

LIS[0] = A[0]
for i in range(1, N):
    if LIS[-1]<A[i]:
        LIS.append(A[i])
    else:
        idx = binary_search(A[i])
        LIS[idx] = A[i]

print(len(LIS))
