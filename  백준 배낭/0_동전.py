# https://habbn-unitystudy.tistory.com/7
# https://edder773.tistory.com/269
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    MONEY = int(input())
    arr = [0]*(MONEY+1)
    arr[0] = 1

    for current_coin in coins:
        for j in range(1, MONEY+1):
            if j>=current_coin:
                arr[j] += arr[j - current_coin]
    print(arr[MONEY])
