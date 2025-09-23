def solution(num_list):
    answer = num_list[:]
    last, prev = answer[-1], answer[-2]
    answer.append(last - prev if last > prev else last * 2)
    return answer