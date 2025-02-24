import sys
sys.stdin = open('input.txt', 'r')

R, C, M = map(int, input().split())
shk = []
for _ in range(M):
    i, j, s, d, z = list(map(int, input().split()))
    shk.append([i-1, j-1, s, d, z])

W, H = 2*C-2, 2*R-2
wtbl = [n for n in range(C)]+[n for n in range(C-2, 0, -1)]
htbl = [n for n in range(R)]+[n for n in range(R-2, 0, -1)]
opp = {1:2, 2:1, 3:4, 4:3}

# [0]:i, [1]:j, [2]:speed, [3]:dir, [4]:size
ans = 0
shk.sort(key=lambda x:(x[1],x[0]))  # 열, 행 오름차순 정렬
for j in range(C): # 0열~ C-1열까지 처리
    #[1] j열의 가장 위 상어를 잡기, j열에서 처음 만난 상어
    for i in range(len(shk)):
        if shk[i][1]==j:
            ans += shk[i][4]
            shk.pop(i)
            break
    # [2] 상어이동
    for i in range(len(shk)):
        if shk[i][3]>=3:    # 우/좌 방향인 경우(한꺼번에 처리가능)
            dr=1 if shk[i][3]==3 else -1    # 우측방향(3) 이면 더하기
            shk[i][1] = (shk[i][1]+shk[i][2]*dr)%W
            if C<=shk[i][1]:
                shk[i][1]=wtbl[shk[i][1]]   # 좌표변환
                shk[i][3]=opp[shk[i][3]]    # 방향반대
        else:                               # 하(2)/상 방향
            dr=1 if shk[i][3]==2 else -1    # 하(2) 이면 더하기
            shk[i][0] = (shk[i][0]+shk[i][2]*dr)%H
            if R<=shk[i][0]:
                shk[i][0]=htbl[shk[i][0]]   # 좌표변환
                shk[i][3]=opp[shk[i][3]]    # 방향반대

    # [3] 상어정렬 후 아래서부터 작은상어가 같은 좌표면 삭제
    shk.sort(key=lambda x:(x[1],x[0],-x[4]))    # 열, 행 오름차순, 크기는 내림차순
    for i in range(len(shk)-1, 0, -1):          # 가장 끝에서 1번까지
        # 위의 상어가 나와 좌표가 같다면 나를 삭제(크기 내림차순이니까)
        if (shk[i][:2])==(shk[i-1][:2]):
            shk.pop(i)
print(ans)
