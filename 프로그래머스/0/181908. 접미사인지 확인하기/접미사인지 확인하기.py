def solution(my_string, is_suffix):
    set_suffix = set([my_string[i:] for i in range(len(my_string))])
    return 1 if is_suffix in set_suffix else 0