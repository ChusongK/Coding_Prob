import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, alst, blst):
    global ans
    # 가지치기: 이미 0이면 더 줄일 가능성 없음!
    # if ans==0:
    #     return
    # 한팀이 이미 M명 초과인 경우
    if len(alst)>M or len(blst)>M:
        return

    if n==N:
        if len(alst)==len(blst):    # 같은 인원수로 팀을 구성
            asm = bsm = 0
            for i in range(M):
                for j in range(M):
                    asm += arr[alst[i]][alst[j]]
                    bsm += arr[blst[i]][blst[j]]

            ans = min(ans, abs(asm - bsm))
        return

    dfs(n+1, alst+[n], blst) # A팀 선택
    dfs(n+1, alst, blst+[n])    # B팀 선택

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

M = N//2
ans = 100*M*M
dfs(0, [], [])
print(ans)
