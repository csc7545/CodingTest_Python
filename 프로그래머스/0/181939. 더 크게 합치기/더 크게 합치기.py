def solution(a, b):
    ba = int(f'{a}' + f'{b}')
    ab = int(f'{b}' + f'{a}')
    answer = max(ba, ab)
    return answer