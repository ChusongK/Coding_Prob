import sys; input = sys.stdin.readline

n, x = map(int, input().split())
day = list(map(int, input().split()))

if max(day) == 0:
    print('SAD')
    exit(0)

value = sum(day[:x]) # 일단 0번째부터 x번째 전까지 sum
max_value = value
max_cnt = 1

# 슬라이딩 윈도우 (한 칸씩 옆으로 옮겨가며 이전 값 최대한 활용)
for i in range(x, n):
    value += day[i] # 뒤에 값 더해주기
    value -= day[i-x] # 앞에 값 빼주기

    if value > max_value:
        max_value = value
        max_cnt = 1 # 카운트 초기화
    elif value == max_value:
        max_cnt += 1

print(max_value)
print(max_cnt)
# 출처: https://lvolz.tistory.com/67 [sing:티스토리]