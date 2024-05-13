def solution(s):
    last_pos = {}
    result = []

    for i, char in enumerate(s):
        if char in last_pos:
            result.append(i - last_pos[char])
        else:
            result.append(-1)
        last_pos[char] = i

    return result