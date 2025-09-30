def solution(my_strings, parts):
    answer = []
    for idx in range(0, len(my_strings)):
        s, e = parts[idx]
        substr = my_strings[idx][s:e+1]
        answer.append(substr)
    return ''.join(answer)