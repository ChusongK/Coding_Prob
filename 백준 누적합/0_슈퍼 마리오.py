import sys
sys.stdin = open('input.txt', 'r')

score = 0

for _ in range(10):
    cur = int(input())
    score += cur
    if score>=100:
        if score - 100 > 100 - (score - cur):
            score -= cur
        break
print(score)