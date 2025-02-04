# https://lvolz.tistory.com/67
import sys
sys.stdin = open('input.txt', 'r')

N, X = map(int, input().split())
visits = list(map(int, input().split()))
cum = [0]*(N+1)

total = 0
for i in range(N):
    total += visits[i]
    cum[i+1] = total

visit_for_X_days = dict()
left = 0
right = X

while right<=N:
    X_days_visits = cum[right]-cum[left]
    if X_days_visits in visit_for_X_days.keys():
        visit_for_X_days[X_days_visits] += 1
    else:
        visit_for_X_days[X_days_visits] = 1
    left += 1
    right += 1

sorted_keys = sorted(visit_for_X_days.keys())
max_visits_for_X_days = sorted_keys[-1]

if max_visits_for_X_days==0:
    print('SAD')
else:
    print(max_visits_for_X_days)
    print(visit_for_X_days[max_visits_for_X_days])
print(sorted_keys)