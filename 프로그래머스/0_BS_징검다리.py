def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    start = 1
    end = distance

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        current = 0

        for rock in rocks:
            if rock - current < mid:
                cnt += 1
            else:
                current = rock
        if cnt > n:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid

    return answer