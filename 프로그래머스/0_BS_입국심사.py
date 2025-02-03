def solution(n, times):
    answer = 0

    start = 0
    end = n * max(times)

    while start <= end:
        mid = (start + end) // 2
        cnt = 0

        for t in times:
            cnt += (mid // t)
        if cnt >= n:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1

    return answer