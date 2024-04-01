def solution(my_string, index_list):
    char_list = list(my_string)
    result = ''.join([char_list[index] for index in index_list])
    return result