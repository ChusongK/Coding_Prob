# https://edder773.tistory.com/64
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for _ in range(T):
    N = int(input())
    a = 1
    b = 0

    for i in range(1, N+1):
        a, b = b, a + b
    print(a, b)

