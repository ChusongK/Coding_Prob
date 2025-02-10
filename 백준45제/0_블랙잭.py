import sys
sys.stdin = open('input.txt', 'r')

def solve():
    max_sum = float('-inf')

    for a in range(N-2):
        for b in range(a+1, N-1):
            for c in range(b+1, N):
                total = lst[a]+lst[b]+lst[c]
                if total<=M:
                    max_sum = max(max_sum, total)
    return max_sum

N, M = map(int, input().split())
lst = list(map(int, input().split()))
ans = solve()
print(ans)