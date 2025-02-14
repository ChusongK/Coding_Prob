from collections import deque

q = deque([(1,2), (2,1), (3,4)])
q.remove((2,1))
print(q)
