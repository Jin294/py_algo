def solution(intStrs, k, s, l):
    return [int(num_str[s:s+l]) for num_str in intStrs if int(num_str[s:s+l]) > k]