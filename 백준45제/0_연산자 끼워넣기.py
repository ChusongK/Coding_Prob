import sys
sys.stdin = open('input.txt', 'r')

def calc(lst):
    # print(lst)
    total = A[0]
    # print(total)

    for i in range(1, N):
        now_op = lst[i-1]
        if now_op==0:
            total += A[i]
            # print(total)
        elif now_op==1:
            total -= A[i]
        elif now_op==2:
            total = total*A[i]
        else:
            if total<0:
                total = (-1)*(((-1)*total)//A[i])
            else:
                total = total//A[i]
    # print(total)
    return total

def dfs(n, lst):
    global mn, mx

    if n==N-1:
        # print('hi')
        res = calc(lst)
        mn = min(mn, res)
        mx = max(mx, res)
        return

    for i in range(N-1):
        if not v[i]:
            # print(n, v)
            v[i]=1
            dfs(n+1, lst+[op[i]])
            v[i]=0

N = int(input())
A = list(map(int, input().split()))
tmp = list(map(int, input().split()))
op = []
for i, val in enumerate(tmp):
    if val==0:  continue
    op += [i]*val
v = [0]*(N-1)

mn, mx = float('inf'), float('-inf')
dfs(0, [])

print(mx)
print(mn)
