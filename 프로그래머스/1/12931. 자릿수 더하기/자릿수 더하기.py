def solution(n):
    answer = 0
    rist = list(str(n))
    for i in range(len(rist)):
        answer += int(rist[i])

    return answer