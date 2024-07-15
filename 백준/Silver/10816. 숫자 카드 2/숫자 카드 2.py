from collections import Counter
import sys

input = sys.stdin.read
data = input().split()

# 입력 처리
N = int(data[0])
cards = list(map(int, data[1:N + 1]))
M = int(data[N + 1])
targets = list(map(int, data[N + 2:]))

# 상근이가 가진 숫자 카드의 빈도를 세기
card_count = Counter(cards)

# 결과 생성
result = [card_count[target] for target in targets]

# 결과 출력
print(' '.join(map(str, result)))