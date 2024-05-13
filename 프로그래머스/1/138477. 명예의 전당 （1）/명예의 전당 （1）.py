import heapq

def solution(k, score):
    hall_of_fame = []
    result = []

    for day, s in enumerate(score):
        if day < k:
            heapq.heappush(hall_of_fame, s)
        else:
            if s > hall_of_fame[0]:
                heapq.heappop(hall_of_fame)
                heapq.heappush(hall_of_fame, s)

        result.append(hall_of_fame[0])
    return result