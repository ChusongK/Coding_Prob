import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
card = list(map(int, input().split()))
card.sort()

M = int(input())
num = list(map(int, input().split()))

card_dict = {}

for c in card:
    if c in card_dict.keys():
        card_dict[c] += 1
    else:
        card_dict[c] = 1

sorted_card = sorted(card_dict.keys())

for i in num:
    start = 0
    end = len(sorted_card)-1

    is_exist = False
    while start<=end:
        mid = (start+end)//2
        if sorted_card[mid]==i:
            is_exist = True
            break
        if sorted_card[mid]<i:
            start = mid + 1
        else:
            end = mid -1
    print(card_dict[i] if is_exist else 0, end=' ')