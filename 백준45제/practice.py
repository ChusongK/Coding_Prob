import sys

sys.stdin = open('input.txt', 'r')


from collections import deque

q = deque()
q.append((3, 3))

a, b = q[-1]
print(a, b)