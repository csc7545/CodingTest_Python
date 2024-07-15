def max_lan_length(K, N, lan_lengths):
    # 이분 탐색 범위를 설정
    left, right = 1, max(lan_lengths)
    
    # 이분 탐색을 통해 최대 랜선 길이 찾기
    result = 0
    while left <= right:
        mid = (left + right) // 2
        
        # mid 길이로 랜선 몇 개를 만들 수 있는지 계산
        count = sum(length // mid for length in lan_lengths)
        
        if count >= N:
            result = mid  # 가능한 최대 길이 업데이트
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# 입력 받기
K, N = map(int, input().split())
lan_lengths = [int(input()) for _ in range(K)]

# 결과 출력
print(max_lan_length(K, N, lan_lengths))
