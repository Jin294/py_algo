def solution(my_strings, parts):
    answer = []
    for my_string, (s, e) in zip(my_strings, parts):
        answer.append(my_string[s:e+1])
    return ''.join(answer)