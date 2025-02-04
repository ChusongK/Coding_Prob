import sys
sys.stdin = open('input.txt', 'r')
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())

cum = [0]*(N+1)
total = 0

for i in range(N):
    total += A[i]
    cum[i+1] = total

for _ in range(M):
    i, j = map(int, input().split())
    print(cum[j]-cum[i-1])