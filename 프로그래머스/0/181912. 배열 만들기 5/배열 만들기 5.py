def solution(intStrs, k, s, l):
    answer = []
    for string in intStrs:
        num_str = int(string[s:s+l])
        if num_str > k:
            answer.append(num_str)
    return answer