import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
nums = sorted(list(map(int, input().split())))
m = int(input())

low, high = 0, max(nums)  # 최소, 최대

answer = 0  # 최종 정답 저장
while low <= high:
    total = 0
    mid = (low + high) // 2  # 중간값

    for num in nums:  # 예산에 따라 추가
        total += min(num, mid)

    if total <= m:  # 한도를 넘지 않는 경우
        low = mid + 1
        answer = mid
    else:  # 한도 초과인 경우
        high = mid - 1

print(answer)