n, k = map(int, input().split())
S = list(map(int, input().split()))

lt = 0  # 왼쪽 포인터
rt = 0  # 오른쪽 포인터
cnt, res = 0, 0  # cnt: 현재 제거한 홀수 개수, res: 최대 길이

while rt < n:  # rt가 배열 끝까지 갈 때까지 진행
    if cnt > k:  # 홀수를 k개 초과로 제거한 경우
        if S[lt] % 2 == 1:  # lt가 가리키는 값이 홀수면 제거 개수 줄임
            cnt -= 1
        lt += 1  # lt를 오른쪽으로 이동
        continue  # 다시 체크

    else:
        if S[rt] % 2 == 1:  # 현재 rt 위치가 홀수라면
            cnt += 1  # 제거한 홀수 개수 증가
        rt += 1  # rt를 오른쪽으로 이동

    res = max(res, rt - lt - cnt)  # 최대 짝수 부분 수열 길이 업데이트

print(res)  # 최대 길이 출력