import sys
sys.stdin = open('input.txt', 'r')

def left(arr):
    narr = []
    for row in arr:
        lst = []
        t = 0
        for e in row:
            if e==0:
                continue
            else:
                if t==0:
                    t=e
                    lst.append(e)
                else:
                    if t==e:
                        lst.pop()
                        lst.append(e*2)
                        t = 0
                    else:
                        lst.append(e)
                        t = e
        narr.append(lst + (N-len(lst))*[0])
    return narr

def dfs(n, arr):
    global ans

    if n==5:
        mx = max(map(max, arr))
        ans = max(ans, mx)
        return

    narr = left(arr)
    dfs(n+1, narr)  # 좌

    narr = [x[::-1] for x in arr]
    narr = left(narr)
    dfs(n+1, narr)  # 우

    arr_t = list(map(list, zip(*arr)))
    narr = left(arr_t)
    dfs(n+1, narr)  # 상

    narr = [x[::-1] for x in arr_t]
    narr = left(narr)
    dfs(n + 1, narr)    # 하

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = float('-inf')
dfs(0, arr)
print(ans)