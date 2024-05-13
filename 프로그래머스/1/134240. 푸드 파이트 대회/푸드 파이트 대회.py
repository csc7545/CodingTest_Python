def solution(food):
    result = ['0']
    left, right = [], []
    
    for i in range(1, len(food)):
        half = food[i] // 2
        left += [str(i)] * half
        right = [str(i)] * half + right
    
    result = ''.join(left + result + right)
    return result