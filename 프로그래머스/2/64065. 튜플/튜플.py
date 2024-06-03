def solution(s):
    s = s[2:-2].split("},{")
    sets = [set(map(int, x.split(','))) for x in s]
    
    sets.sort(key=len)

    result = []
    seen = set()
    
    for s in sets:
        new_element = (s - seen).pop()
        result.append(new_element)
        seen.update(s)
    
    return result