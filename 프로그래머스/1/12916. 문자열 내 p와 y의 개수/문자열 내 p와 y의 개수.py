def solution(s):
    answer = True
    s = s.lower()
    
    if(s.count('y') == s.count('p')):
        answer = True
    elif(s.count('y') != s.count('p')):
        answer = False
    else:
        answer = True

    return answer