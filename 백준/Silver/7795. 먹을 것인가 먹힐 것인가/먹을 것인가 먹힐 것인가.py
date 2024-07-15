import sys
import bisect

input = sys.stdin.read
data = input().split()

idx = 0
T = int(data[idx])
idx += 1

results = []

for _ in range(T):
    N = int(data[idx])
    M = int(data[idx + 1])
    idx += 2

    A = list(map(int, data[idx:idx + N]))
    B = list(map(int, data[idx + N:idx + N + M]))
    idx += (N + M)

    A.sort()
    B.sort()

    count = 0

    # A의 각 원소에 대해 B에서 이진 탐색으로 작은 원소의 개수를 찾음
    for a in A:
        count += bisect.bisect_left(B, a)

    results.append(count)

for result in results:
    print(result)
