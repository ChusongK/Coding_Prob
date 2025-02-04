import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
liquids = list(map(int, input().split()))

min_sum = sys.maxsize
combi = [0, 0]

for i in range(len(liquids)-1):
    current_liquid = liquids[i]
    start = i+1
    end = len(liquids)-1

    while start<=end:
        mid = (start+end)//2
        current_sum = current_liquid+liquids[mid]
        # 합의 절대값이 0에 더 가까우면, 최솟값 갱신
        if abs(current_sum)<min_sum:
            min_sum = abs(current_sum)
            combi[0], combi[1] = liquids[i], liquids[mid]
            if current_sum==0:
                break
        if current_sum<0:
            start = mid+1
        else:
            end = mid-1

print(combi[0], combi[1])

