# https://m.blog.naver.com/jiyong615/222080343707
import sys
sys.stdin = open('input.txt', 'r')

N, C = map(int, input().split())
home = [int(input()) for _ in range(N)]
home.sort()

start = 1
end = home[-1] - home[0]

ans = 0
while start<=end:
    mid = (start+end)//2
    current = home[0]
    cnt = 1

    for i in range(1, len(home)):
        if home[i]>=current+mid:
            cnt += 1
            current = home[i]
    if cnt>=C:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
print(ans)