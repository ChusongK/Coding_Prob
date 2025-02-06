# https://www.google.com/search?q=%EB%B0%B1%EC%A4%80+12869+%ED%8C%8C%EC%9D%B4%EC%8D%AC&sca_esv=744faba34f407743&biw=1266&bih=1346&sxsrf=AHTn8zrPXKO31CQP_wJPgbEg9omU8ZbStw%3A1738803022484&ei=TgekZ7SaHf2Uvr0P9NPX0QU&oq=12869+%EB%AE%A4%ED%83%88%EB%A6%AC%EC%8A%A4%ED%81%AC&gs_lp=Egxnd3Mtd2l6LXNlcnAiFTEyODY5IOuupO2DiOumrOyKpO2BrCoCCAAyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEdI6wZQAFgAcAF4AJABAJgBpAGgAaQBqgEDMC4xuAEByAEAmAIBoAIHmAMAiAYBkAYKkgcBMaAH2AU&sclient=gws-wiz-serp

n = int(input())
scv = list(map(int, input().split()))
scv.extend([0, 0]) #3개 미만이 들어왔을 때 개수 맞춰주기

dp = [[[0]*61 for _ in range(61)] for _ in range(61)] #각 위치에 도달하는 횟수 저장
dp[scv[0]][scv[1]][scv[2]] = 1 #초기화, 0인데 1로 초기화했으므로 나중에 1 빼주기

comb = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]
for i in range(60, -1, -1):
    for j in range(60, -1, -1):
        for k in range(60, -1, -1):
            if dp[i][j][k] > 0:
                for c in comb:
                    i_ = i-c[0] if i-c[0] >= 0 else 0
                    j_ = j-c[1] if j-c[1] >= 0 else 0
                    k_ = k-c[2] if k-c[2] >= 0 else 0
                    if dp[i_][j_][k_] == 0 or dp[i_][j_][k_] > dp[i][j][k]+1:
                    # 처음 도착한 경우 or 더 적은 횟수로 도착하는 경우에만 업데이트
                        dp[i_][j_][k_] = dp[i][j][k]+1

print(dp[0][0][0]-1)