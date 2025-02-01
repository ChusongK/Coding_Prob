import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
plan = list(map(int, input().split()))
plan.sort()
money = int(input())

if sum(plan)<=money:
    print(plan[-1])
else:
    ans = 0
    start = money//len(plan)
    end = plan[-1]

    while start<=end:
        mid = (start+end)//2
        s = 0
        for i in plan:
            if i<=mid:
                s+=i
            else:
                s+=mid
        if s<=money:
            start = mid+1
            ans = mid
        else:
            end = mid-1
    print(ans)