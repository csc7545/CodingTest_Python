from itertools import combinations

def solution(number):
    count = 0
    
    for combo in combinations(number, 3):
        if sum(combo) == 0:
            count += 1
            
    return count

if __name__ == "__main__":
    number = list(map(int, input().strip().split()))
    result = solution(number)
    print(result)