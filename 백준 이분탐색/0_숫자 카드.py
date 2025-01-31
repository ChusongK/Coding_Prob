import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
card = list(map(int, input().split()))
card.sort()

M = int(input())
num = list(map(int, input().split()))

for i in num:
    start = 0
    end = len(card)-1
    is_exist = False

    while start<=end:
        mid = (start+end)//2
        if card[mid]==i:
            is_exist = True
            break
        if card[mid]<i:
            start = mid + 1
        else:
            end = mid - 1
    print(1 if is_exist else 0, end = ' ')