# https://velog.io/@hamsangjin/%EB%B0%B1%EC%A4%80-10816%EB%B2%88-%EC%88%AB%EC%9E%90-%EC%B9%B4%EB%93%9C-2-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
card = list(map(int, input().split()))

M = int(input())
num = list(map(int, input().split()))

card_dict = {}
for c in card:
    if c in card_dict.keys():
        card_dict[c] += 1
    else:
        card_dict[c] = 1

for n in num:
    print(card_dict[n] if n in card_dict.keys() else 0, end = ' ')