# https://velog.io/@deannn/BOJ-%EB%B0%B1%EC%A4%80-1920%EB%B2%88-%EC%88%98-%EC%B0%BE%EA%B8%B0-Python
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
for i in map(int, input().split()):
    start = 0
    end = N-1
    is_exist = False

    while start<=end:
        mid = (start+end)//2
        if A[mid]==i:
            is_exist = True
            break
        if A[mid]<i:
            start = mid + 1
        else:
            end = mid - 1
    print(1 if is_exist else 0)
