import sys
sys.stdin = open('input.txt', 'r')

def check(lst, v):
    cnt = 1
    for i in range(1, N):
        if lst[i-1]==lst[i]:
            cnt += 1
        elif lst[i-1]+1==lst[i] \
            and v[i-L:i]==[0]*L \
            and cnt>=L:
            v[i-L:i] = [1]*L
            cnt = 1
        elif lst[i-1]>lst[i]:
            cnt = 1
        else:
            return False
    return True

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for _ in range(2):
    for lst in arr:
        v = [0]*N
        if check(lst, v) and check(lst[::-1], v[::-1]):
            ans += 1
    arr = list(map(list, zip(*arr)))
print(ans)