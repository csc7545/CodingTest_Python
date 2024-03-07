def solution(n):
    return next(x for x in range(1,n) if n % x == 1)